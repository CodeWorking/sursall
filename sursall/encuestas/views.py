from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from models import Contacto, Comentario
from django.contrib.auth.models import User




def bienvenido(request):
    
    return render_to_response('bienvenido.html', {}, context_instance=RequestContext(request))

def base(request):
    
    return render_to_response('base.html', {}, context_instance=RequestContext(request))

def nuevousuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html', {'formulario':formulario}, context_instance=RequestContext(request))


def ingresar(request):
    #if not request.user.is_anonymous():
        #return HttpResponseRedirect('/ingresar')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/bienvenido')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html', {'formulario':formulario}, context_instance=RequestContext(request))

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde Diego'
            contenido = formulario.cleaned_data ['mensaje'] + "\n"
            contenido += 'Comunicarse a:' + formulario.cleaned_data ['correo']
            correo = EmailMessage(titulo, contenido, to=['alejandrorodriguezperalta@gmail.com'])
            correo.send()
            return HttpResponseRedirect('/')
    else:
         formulario = ContactoForm()
    return render_to_response('Contactenos.html', {'formulario':formulario}, context_instance=RequestContext(request))
                
 










