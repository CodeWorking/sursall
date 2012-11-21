#encoding:utf-8
from django.db import models
import datetime

CHOICES_TIPO_PREGUNTA = ((0,"Seleccion Multiple"),(1, "Pregunta Abiertas"),(1, "Pregunta Reflexivas"),(1, "Pregunta Cerradas"),(1, "Pregunta Verdadero  - Falso"),(1, "Pregunta Abiertas"))
CHOICES_TIPO_USUARIO = ((0,"Psicologo"),(1, "Estudiante"))

Contacto = models.CharField(max_length=70)
Comentario = models.CharField(max_length=70)

class Persona(models.Model):
    edad = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    tipo_usuario = models.IntegerField(choices=CHOICES_TIPO_USUARIO)
    usuario = models.OneToOneField("auth.User")

    def __unicode__(self):
        
        return "%s" % (self.usuario)

class Prueba(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
            
    def __unicode__(self):
        return "%s" % (self.nombre)



class Modulo(models.Model):  
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    prueba = models.ForeignKey(Prueba)
    
    def secciones_por_contestar(self, persona):
        mr = self.seccion_set.exclude(seccioncontestada__usuario=persona, seccioncontestada__fecha_final__isnull=False)
        return mr.count()
    
    def secciones_contestadas(self, persona):
        sc = self.seccion_set.filter(seccioncontestada__usuario=persona, seccioncontestada__fecha_final__isnull=True)
        return sc.count()
         
    def __unicode__(self):
        return "%s en %s" % (self.nombre, self.prueba)


    
class Seccion(models.Model):
    nombre = models.CharField(max_length=30)
    instruccion = models.TextField()
    modulo = models.ForeignKey(Modulo)
    
    def preguntas_sin_contestar(self, persona):
        r = self.seccioncontestada_set.filter(usuario=persona)
        if r.count() > 0:
            return r[0].preguntas_a_contestar().count()
        else:
            return self.pregunta_set.count()  
  
    def __unicode__(self):
        return "%s en %s" % (self.nombre, self.modulo)


class Pregunta(models.Model):
    orden = models.IntegerField()
    descripcion_text = models.TextField()
    #descripcion_imag = models.ImageField(upload_to='imagen')
    tiempo = models.IntegerField(null=True, blank=True)
    tipo_pregunta = models.IntegerField(choices=CHOICES_TIPO_PREGUNTA)
    seccion = models.ForeignKey(Seccion)
    
    class Meta:
        unique_together = (("orden", "seccion"))

    def __unicode__(self):
        return "%s la %s" % (self.orden, self.seccion)


class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    descripcion = models.TextField()    
    orden = models.IntegerField ()
    puntaje = models.IntegerField()

    @property
    def orden_letra(self):
        return chr(ord("A") + self.orden-1) 
    
    class Meta:
        unique_together = (("orden", "pregunta"))
    
    def __unicode__(self):
        return "%s en %s" % (self.orden, self.pregunta)


class SeccionContestada(models.Model):
    seccion = models.ForeignKey(Seccion)
    fecha_inicio = models.DateTimeField(default=datetime.datetime.now)
    fecha_final = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(Persona)

    class Meta:
        unique_together = (("seccion", "usuario"))
            
    def preguntas_a_contestar(self):
        return self.seccion.pregunta_set.exclude(seleccion__seccion_contestada__usuario=self.usuario).order_by("orden")
   
    def __unicode__(self):
        return "%s la %s" % (self.seccion, self.fecha_inicio)


class Seleccion(models.Model):
    respuesta = models.ForeignKey(Respuesta)
    pregunta = models.ForeignKey(Pregunta)
    seccion_contestada = models.ForeignKey(SeccionContestada)

    class Meta:
        unique_together = (("pregunta", "seccion_contestada"))

    def __unicode__(self):
        return "%s la %s" % (self.respuesta, self.seccion_contestada)
