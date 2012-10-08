from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth import authenticate


def home(request):
    
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def autenticacion(request):
    
    return render_to_response('autenticacion.html', {}, context_instance=RequestContext(request))

