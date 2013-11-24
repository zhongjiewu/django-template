import hashlib
import json
import os
import re

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.core import exceptions

from forms import UploadDataFileForm
from logic.controller import fetch_similar_items
from logic.controller import save_domain_config
from raas.models.control import DomainConfig

DATA_FILE_DIR = "data"


def handle_uploaded_file(f, domain):
    try:
        data_dir = os.path.join(settings.MEDIA_ROOT, DATA_FILE_DIR)

        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        md5 = hashlib.md5()
        md5.update(f.read())
        md5sum = md5.hexdigest()
        ext = os.path.splitext(f.name)[1]
        folder = os.path.join(data_dir, str(domain.id))
        filename = md5sum + ext
        filepath = os.path.join(folder, filename)
        if not os.path.exists(folder):
            os.mkdir(folder)
        with open(filepath, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return True, filename, None
    except Exception, e:
        return False, "", str(e)


@csrf_exempt
def setup_domain(request):
    if request.method == 'POST':
        try:
            config = json.loads(request.body)
        except ValueError:
            return HttpResponse(json.dumps({'result': "Bad JSON"}), content_type="application/json", status=400)
        status, msg = save_domain_config(request.user.id, config['domain_name'], config['indexes'])
        if not status:
            return HttpResponse(json.dumps({'result': msg}), status=400, content_type="application/json")
        return HttpResponse(json.dumps({'result': "success"}), content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({'result': "Method not supported. Must be POST"}),
            content_type="application/json", status=405
        )


@csrf_exempt
def upload_data(request):
    if request.method == 'POST':
        data_form = UploadDataFileForm(request.POST, request.FILES)
        if data_form.is_valid():
            domain_name = request.REQUEST['domain']
            domain = None
            try:
                domain = DomainConfig.objects.get(
                    user_id=request.user.id,
                    domain__exact=domain_name)
            except exceptions.ObjectDoesNotExist:
                return HttpResponse(
                    json.dumps({'result': "Domain not found"}),
                    content_type="application/json",
                    status=404
                )
            result, filename, msg = handle_uploaded_file(request.FILES['datafile'], domain)
            domain.filename = filename
            domain.save()
            if result:
                return HttpResponse(
                    json.dumps({'result': "Success"}),
                    content_type="application/json"
                )
            else:
                return HttpResponse(
                    json.dumps({'result': msg}),
                    content_type="application/json", status=500
                )
        else:
            return HttpResponse(
                json.dumps({'result': data_form.errors}),
                content_type="application/json", status=400
            )
    return HttpResponse(json.dumps(
        {'result': "Method not supported. Must be POST"}),
        content_type="application/json", status=405
    )


def similar_items_demo(request):
    for key in ["item_id", "callback"]:
        if key not in request.GET:
            return HttpResponseBadRequest("%s is not specified" % key)
    pid = request.GET["item_id"]
    callback = request.GET["callback"]
    if not re.match("^[a-zA-Z_][a-zA-Z0-9_]*$", callback):
        return HttpResponseBadRequest("Illegal characters in callback. Must only contain letters" +
                                      " numbers or underscore but not start with number")
    #place holder, return hardcoded data
    items = fetch_similar_items(pid)
    results = {
        "count": len(items),
        "similar_items": items}
    jsonp = "window.RaaS && window.RaaS.callbacks && window.RaaS." + \
        "callbacks.%s && window.RaaS.callbacks.%s.call(window,%s)" % (callback, callback, json.dumps(results))
    return HttpResponse(jsonp, content_type="application/x-javascript")