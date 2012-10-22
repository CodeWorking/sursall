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
from encuestas.forms import ContactoForm
from encuestas import models
from django.contrib.auth.decorators import login_required

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/') 

@login_required
def bienvenido(request):
    
    try:
        persona = request.user.persona
    except:
        # TODO: error para cuando el user no tiene persona
        return render_to_response('bienvenido.html', {}, context_instance=RequestContext(request))
    if persona.tipo_usuario == 0:
        return HttpResponseRedirect('administrador')  
    else:
        pass 
    return render_to_response('bienvenido.html', {}, context_instance=RequestContext(request))

def administrador(request):
    return render_to_response('administrador.html', {}, context_instance=RequestContext(request))

@login_required
def base(request):
    
    return render_to_response('base.html', {}, context_instance=RequestContext(request))

def ingresar(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('bienvenido')
                else:
                    formulario = AuthenticationForm()
                    return render_to_response('ingresar.html', {'mensaje':" El usuario digitado no se encuetra activo, Por favor contactese con el administrador ", 'formulario':formulario}, context_instance=RequestContext(request))
                    
            else:
                    formulario = AuthenticationForm()
                    return render_to_response('ingresar.html', {'mensaje':" La combinacion de usuario y password no es correcta intente de nuevo ", 'formulario':formulario}, context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html', {'formulario':formulario}, context_instance=RequestContext(request))

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde Vocacionalsoft'
            contenido = formulario.cleaned_data ['mensaje'] + "\n"
            contenido += 'Comunicarse a:' + formulario.cleaned_data ['correo']
            correo = EmailMessage(titulo, contenido, to=['alejandrorodriguezperalta@gmail.com'])
            correo.send()
            return render_to_response('Contactenos.html', {'mensaje':" Se ha enviado satisfactoriamente sus solicitudes "}, context_instance=RequestContext(request))
    else:
        formulario = ContactoForm()
    return render_to_response('Contactenos.html', {'formulario':formulario}, context_instance=RequestContext(request))

@login_required 
def prueba(request, id_prueba):
    models.Prueba.objects.get(id=id_prueba)
    







