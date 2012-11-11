#encoding:utf-8
from django.db import models

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
    
    def __unicode__(self):
        return "%s en %s" % (self.nombre, self.prueba)


    
class Seccion(models.Model):
    nombre = models.CharField(max_length=30)
    instruccion = models.TextField()
    modulo = models.ForeignKey(Modulo)
    
    def __unicode__(self):
        return "%s en %s" % (self.nombre, self.modulo)

class Pregunta(models.Model):
    orden = models.IntegerField()
    descripcion_text = models.TextField()
    #descripcion_imag = models.ImageField(upload_to='imagen')
    tiempo = models.IntegerField(null=True, blank=True)
    tipo_pregunta = models.IntegerField(choices=CHOICES_TIPO_PREGUNTA)
    seccion = models.ForeignKey(Seccion)

    def __unicode__(self):
        return "%s la %s" % (self.orden, self.seccion)

class PruebaContestada(models.Model):
    prueba = models.ForeignKey(Prueba)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Persona)

    def __unicode__(self):
        return "%s la %s" % (self.prueba, self.fecha)

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    descripcion = models.TextField()    
    orden = models.IntegerField ()
    puntaje = models.IntegerField()

    @property
    def orden_letra(self):
        return chr(ord("A") + self.orden-1) 
    
    
    def __unicode__(self):
        return "%s en %s" % (self.orden, self.pregunta)

class Seleccion(models.Model):
    respuesta = models.ForeignKey(Respuesta)

    def __unicode__(self):
        return "%s la %s" % (self.respuesta)

