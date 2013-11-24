import json
from django.core import urlresolvers

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from raas.logic import controller
from raas.models.control import DomainConfig


def landing(request):
    return render_to_response(
        "landing.html",
        context_instance=RequestContext(request)
    )


def new_domain(request):
    return render_to_response(
        "domain_new.html",
        context_instance=RequestContext(request)
    )


def upload_file(request):
    domain_objs = DomainConfig.objects.all()
    domains = []
    for domain_obj in domain_objs:
        domains.append({
            "domain": domain_obj.domain,
            "id": domain_obj.id
        })
    domains_json = json.dumps(domains)
    return render_to_response("upload_file.html", {"domains": domains_json})


def raas_js(request):
    return render_to_response(
        "raas.js",
        {
            "jsonp_url_base": "/demo/api/similar_items"
        },
        content_type="application/x-javascript"
    )


def demo_view(request, pid):
    if pid == '':
        pid = controller.try_fetch_random_items(1)[0]['id']
        return HttpResponseRedirect(urlresolvers.reverse('raas.views.demo_view', args=[str(pid)]))
    item = controller.fetch_item(pid)
    random_items = controller.try_fetch_random_items(8)
    return render_to_response(
        "request_similar_items_demo.html",
        {
          "pid": pid,
          "item_json": json.dumps(item),
          "random_items_json": json.dumps(random_items)
        },
        context_instance=RequestContext(request)
    )

