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
from encuestas.models import SeccionContestada
from encuestas.models import Seleccion
from datetime import datetime
from django.core import exceptions


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
    persona = request.user.persona
    prueba = models.Prueba.objects.get(id=id_prueba)
    modulos = []
    #ssc = models.SeccionContestada.objects.filter(fecha_final = None)
    #print models.Modulo.ssc()
    for m in models.Modulo.objects.filter(prueba__id=id_prueba):
        if m.secciones_por_contestar(persona) > 0: 
            modulos.append(m)
    return render_to_response('prueba.html', {'modulos':modulos, 'prueba':prueba}, context_instance=RequestContext(request))
    
@login_required 
def modulo(request, id_modulo):
    modulo = models.Modulo.objects.get(id=id_modulo)
    secciones = []
    persona = request.user.persona
    for s in models.Seccion.objects.filter(modulo__id=id_modulo):
        if s.preguntas_sin_contestar(persona) > 0:
            secciones.append(s)
    return render_to_response('modulo.html', {'secciones':secciones, 'modulo':modulo}, context_instance=RequestContext(request))

@login_required 
def seccion(request, id_seccion):
    persona = request.user
    sec = models.Seccion.objects.get(id=id_seccion)
    if request.method == 'POST':
        models.competencia_seleccionada.objects.get_or_create(usuario=persona.persona,seccion=sec, competencia=sec.competencia, puntaje=0)
        sec_cont = models.SeccionContestada.objects.get_or_create(seccion=sec, usuario=persona.persona)[0]
        request.session["seccion_contestada"] = sec_cont
        try:
            prs = sec_cont.preguntas_a_contestar()[0].id
            return HttpResponseRedirect('/contestar_pregunta/%s/' % (prs)) 
        except:
            pass
    return render_to_response('seccion.html', {'sec':sec}, context_instance=RequestContext(request))

@login_required 
def pregunta(request, id_pregunta):   
    pregunta = models.Pregunta.objects.get(id=id_pregunta)   
    if request.method == 'POST':     
        pform = PreguntaForm(pregunta, request.POST)
        if pform.is_valid():
            resp = int(pform.cleaned_data["respuestas"])
            models.Seleccion.objects.get_or_create(respuesta=models.Respuesta.objects.get(id=resp),
                                            pregunta=models.Pregunta.objects.get(id=id_pregunta),
                                            seccion_contestada=request.session["seccion_contestada"])
            cmu = models.competencia_seleccionada.objects.get(usuario_id=request.user.persona, seccion=pregunta.seccion)
            rpp = models.Respuesta.objects.get(id=resp).puntaje
            cmu.puntaje = (cmu.puntaje+rpp)
            cmu.save()            
        try:
            prs = request.session["seccion_contestada"].preguntas_a_contestar()[0].id
            return HttpResponseRedirect('/contestar_pregunta/%s/' % (prs)) 
        except:
            SeccionCont = SeccionContestada.objects.get(seccion=pregunta.seccion.id)
            SeccionCont.fecha_final= datetime.now()
            SeccionCont.save()
            m =  pregunta.seccion.modulo.id
            return HttpResponseRedirect('/contestar_modulo/%s/' % (m))              
    else:
        pform = PreguntaForm(pregunta)
    return render_to_response('pregunta.html', {'pregunta':pregunta, 'pform':pform}, context_instance=RequestContext(request))
    
@login_required 
def respuesta(request, id_respuesta):
    persona = request.user
    respuesta = models.Respuesta.objects.get(id=id_respuesta)
    return render_to_response('pregunta.html', {'respuesta':respuesta}, context_instance=RequestContext(request))

@login_required 
def administrador(request):
    sec_enc = models.Persona.objects.filter(seccioncontestada__usuario__isnull=False)
    usu_enc = sec_enc.count()
    return render_to_response('administrador.html', {'usu_enc':usu_enc}, context_instance=RequestContext(request))

@login_required
def base(request):
    return render_to_response('base.html', {}, context_instance=RequestContext(request))

@login_required
def Competencias(request, id_usuario):
    Compt = []   
    for cmp in models.competencia_seleccionada.objects.filter(usuario=id_usuario):
        Compt.append(cmp)
    return render_to_response('Competencias.html', {'Compt':Compt}, context_instance=RequestContext(request))

@login_required
def resultados(request):
    usuario = []
    for s in models.Persona.objects.filter():
        for m in models.Modulo.objects.filter():
            if m.secciones_por_contestar(s)>0:
                usuario.append(s) 
    return render_to_response('adm.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required
def seccion_contestada_resultados(request, id_sec_cont):
    if request.method == 'POST':
        ob = request.POST.get('observaciones')
        seccon = models.SeccionContestada.objects.get(id=id_sec_cont)
        sec = seccon.seccion.id
        compts = models.competencia_seleccionada.objects.filter(seccion=sec)
        cmt =compts.get()
        cmt.observacion = ob
        cmt.save()               
    secrs = SeccionContestada.objects.get(id=id_sec_cont)
    selrs= []   
    for selrp in Seleccion.objects.filter(seccion_contestada_id=id_sec_cont):
        selrs.append(selrp) 
    return render_to_response('adm_gst.html', {'secrs':secrs, 'selrs':selrs}, context_instance=RequestContext(request))

@login_required
def gestionresultados(request, id_usuario):
    secciones = [] 
    for sec in SeccionContestada.objects.filter(usuario=id_usuario):     
        secciones.append(sec)
    return render_to_response('seccion_contestada.html', {'secciones':secciones}, context_instance=RequestContext(request))

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
