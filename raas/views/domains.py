import json
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from raas.models import DomainConfig, Field, RecModel, SearchModel, RankModel


def index(request):
    domain_objs = DomainConfig.objects.all()
    domains = []
    for d in domain_objs:
        domains.append({
            "id": d.id,
            "user_id": d.user.id,
            "domain": d.domain,
            "number_of_rec": d.number_of_rec,
            "filename": d.filename,
            "created": str(d.created),
            "updated": str(d.updated),
            "domain_url": reverse(edit, args=[str(d.id)])
        })
    return render_to_response("domains/index.html", {
        "domains_json": json.dumps(domains)
    })


def edit(request, id):
    domain_obj = DomainConfig.objects.get(id=id)
    field_objs = Field.objects.filter(domain_id=id)
    domain = {
        "id": domain_obj.id,
        "user_id": domain_obj.user_id,
        "domain": domain_obj.domain,
        "number_of_rec": domain_obj.number_of_rec,
        "filename": domain_obj.filename,
        "created": str(domain_obj.created),
        "updated": str(domain_obj.updated)
    }
    fields = []
    for f in field_objs:
        fields.append({
            "id": f.id,
            "name": f.name,
            "ftype": f.ftype,
            'ftype_description': Field.get_field_type(f.ftype),
            "column": f.column
        })

    rec_model = None
    try:
        rec_model_obj = RecModel.objects.get(domain_id=id)
        rec_model = {
            'id': rec_model_obj.id,
            'domain_id': rec_model_obj.domain_id,
            'current_search_model_id': rec_model_obj.current_search_model_id,
            'current_rank_model_id': rec_model_obj.current_rank_model_id,
            'created': str(rec_model_obj.created),
            'updated': str(rec_model_obj.updated),
        }
        try:
            obj = rec_model_obj.current_search_model
            rec_model['current_search_model_name'] = obj.name
        except ObjectDoesNotExist:
            pass
        try:
            obj = rec_model_obj.current_rank_model
            rec_model['current_rank_model_name'] = obj.name
        except ObjectDoesNotExist:
            pass
    except ObjectDoesNotExist:
        pass

    search_models = []
    rank_models = []
    smodel_objects = SearchModel.objects.filter(domain_id=domain_obj.id)
    rmodel_objects = RankModel.objects.filter(domain_id=domain_obj.id)
    for obj in smodel_objects:
        search_models.append({
            'id': obj.id,
            'domain_id': obj.domain_id,
            'name': obj.name,
            'description': obj.description,
            'content': obj.content,
            'created': str(obj.created),
            'updated': str(obj.updated)
        })
    for obj in rmodel_objects:
        rank_models.append({
            'id': obj.id,
            'domain_id': obj.domain_id,
            'name': obj.name,
            'description': obj.description,
            'content': obj.content,
            'created': str(obj.created),
            'updated': str(obj.updated)
        })

    return render_to_response("domains/edit.html", {
        'fields_json': json.dumps(fields),
        'domain_json': json.dumps(domain),
        'rec_model_json': json.dumps(rec_model),
        'search_models_json': json.dumps(search_models),
        'rank_models_json': json.dumps(rank_models),
    })