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
from encuestas.forms import PreguntaForm
from encuestas import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def DevContacto(request):
    if(request.user.is_authenticated):
        if(request.user.id == None):
            return HttpResponseRedirect('/')
        else:
            persona = request.user.persona
            if (persona. tipo_usuario == 0):
                return HttpResponseRedirect('/administrador') 
            else:
                return HttpResponseRedirect('/estudiante')               
    
@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/') 

@login_required 
def estudiante(request):
    pruebas = models.Prueba.objects.all()    
    return render_to_response('estudiante.html', {'pruebas':pruebas}, context_instance=RequestContext(request))
          
@login_required 
def prueba(request, id_prueba):
    prueba = models.Prueba.objects.get(id=id_prueba)
    #print models.Prueba.nombre    
    return render_to_response('prueba.html', {'prueba':prueba}, context_instance=RequestContext(request))
    
@login_required 
def modulo(request, id_modulo):
    modulo = models.Modulo.objects.get(id=id_modulo)
    #print models.Prueba.nombre    
    return render_to_response('modulo.html', {'modulo':modulo}, context_instance=RequestContext(request))

@login_required 
def seccion(request, id_seccion):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        return HttpResponseRedirect('/contestar_pregunta/') 
    else:
        formulario = ContactoForm()
    seccion = models.Seccion.objects.get(id=id_seccion)
    return render_to_response('seccion.html', {'seccion':seccion}, context_instance=RequestContext(request))

@login_required 
def pregunta(request, id_pregunta):
    print "sada"
    pregunta = models.Pregunta.objects.get(id=id_pregunta)
    return render_to_response('pregunta.html', {'pregunta':pregunta}, context_instance=RequestContext(request))

@login_required 
def respuesta(request, id_respuesta):
    respuesta = models.Respuesta.objects.get(id=id_respuesta)
    #print models.Prueba.nombre    
    return render_to_response('pregunta.html', {'respuesta':respuesta}, context_instance=RequestContext(request))

@login_required 
def administrador(request):
    Name = models.PruebaContestada.objects.count()
    return render_to_response('administrador.html', {'Name':Name}, context_instance=RequestContext(request))

@login_required
def base(request):
    return render_to_response('base.html', {}, context_instance=RequestContext(request))

def ingresar(request):
    if(request.user.is_authenticated):
        if(request.user.id == None):    
            if request.method == 'POST':
                formulario = AuthenticationForm(request.POST)
                if formulario.is_valid:
                    usuario = request.POST['username']
                    clave = request.POST['password']
                    acceso = authenticate(username=usuario, password=clave)
                    if acceso is not None:
                        if acceso.is_active:
                            login(request, acceso)
                            persona = request.user.persona
                            if (persona. tipo_usuario == 0):
                                return HttpResponseRedirect('administrador')
                            else:
                                return HttpResponseRedirect('estudiante')  
                        else:
                            formulario = AuthenticationForm()
                            return render_to_response('ingresar.html', {'mensaje':" El usuario digitado no se encuetra activo, Por favor contactese con el administrador ", 'formulario':formulario}, context_instance=RequestContext(request))
                    else:
                            formulario = AuthenticationForm()
                            return render_to_response('ingresar.html', {'mensaje':" La combinacion de usuario y password no es correcta intente de nuevo ", 'formulario':formulario}, context_instance=RequestContext(request))
            else:
                formulario = AuthenticationForm()
            return render_to_response('ingresar.html', {'formulario':formulario}, context_instance=RequestContext(request))
        else:
            persona = request.user.persona
            if (persona. tipo_usuario == 0):
                return HttpResponseRedirect('administrador')
            else:
                return HttpResponseRedirect('estudiante')  
            
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
