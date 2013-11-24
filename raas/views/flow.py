import json
from django.core import urlresolvers

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from raas.logic import controller
from raas.models.control import DomainConfig


def raas_start(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/users/sign_in")
    return render_to_response(
        "start.html",
        context_instance=RequestContext(request))


def raas_job(request):
    return render_to_response(
        "jobs.html",
        context_instance=RequestContext(request))