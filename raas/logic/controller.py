import json
import os
from django.core.exceptions import ObjectDoesNotExist

from django.forms.models import model_to_dict
from django.conf import settings

from raas.models import DomainConfig
from raas.models import Field
from raas.models import Product
from raas.models import RecModel
from raas.models import RecResults


def save_domain_config(uid, domain, indexes):
    try:
        #TODO: only admin user now.
        dom, _ = DomainConfig.objects.get_or_create(user_id=uid, domain=domain)
    except Exception, e:
        return False, "Invalid domain name, {0}, Exception: {1}".format(domain, e)

    Field.objects.filter(domain_id__exact=dom.id).delete()
    for i, item in enumerate(indexes):
        name = item['name']
        type = item['type']
        fdict = Field.get_field_dict()
        if type not in fdict:
            return False, "Invalid field type: {0} {1}".format(name, type)
        try:
            Field(domain=dom, name=name, ftype=fdict[type], column=int(i)).save()
        except Exception, e:
            return False, "Cannot save field: {0} {1}, Exception: {2}".format(name, type, e)
    return True, None


def fetch_domain_meta(uid, domain):
    result = {}
    try:
        dom = DomainConfig.objects.get(user_id=uid, domain=domain)
        rec_model = RecModel.objects.get(domain_id=dom.id)
        result['domain_id'] = dom.id
        result['domain_name'] = dom.domain
        result['number_rec'] = dom.number_of_rec
        result['field_types'] = {}
        result['id_field'] = 'id'
        result['search_model'] = json.loads(rec_model.current_search_model.content)
        result['rank_model'] = json.loads(rec_model.current_rank_model.content)
        # populate fields
        for f in Field.objects.filter(domain_id=dom.id):
            result['field_types'][f.name] = Field.get_field_type(f.ftype)
    except Exception, e:
        return None, "Error: {0}".format(e)
    return result, None


def fetch_model_from_file(domain, model_type, version):
    """models are saved in data/model/<domain>.
    model files are named as <type>_<version>.dat"""

    model_path = os.path.join(
        settings.PROJECT_ROOT,
        "../data/model",
        str(domain),
        model_type + "_" + str(version) + ".dat")
    try:
        json_data = open(model_path)
        model = json.load(json_data)
        json_data.close()
        return model
    except:
        return None


def fetch_item(pid):
    prod = Product.objects.get(pid=pid)
    return {'id': pid,
            'fields': {'title': prod.title,
                       'link': prod.link,
                       'image': prod.image}}


def try_fetch_random_items(count):
    import random
    items = []
    product_count = Product.objects.count()
    while count > 0:
        random_number = int(random.uniform(0, product_count)) + 1
        try:
            prod = fetch_item(random_number)
            items.append(prod)
        except ObjectDoesNotExist:
            pass
        count -= 1
    return items


def fetch_similar_items(source):
    targets = dict([(t.target, t.score) 
                    for t in RecResults.objects.filter(source=source)
                    if t.target != source])
    products = Product.objects.filter(pid__in=[t for t in targets.iterkeys()])
    items = []
    for t in products:
        prod = fetch_item(t.pid)
        prod['fields']['score'] = targets[t.pid]
        items.append(prod)
    items = sorted(items, key=lambda item: item['fields']['score'], reverse=True)
    return items
