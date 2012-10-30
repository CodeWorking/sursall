#encoding:utf-8
from django.db import models

CHOICES_TIPO_PREGUNTA = ((0,"Una pregunta"),(1, "Segunda Pregunta"))
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
        
    def __unicode__(self):
        return "%s" % (self.nombre)



class Modulo(models.Model):  
    nombre = models.CharField(max_length=50)
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

    def __unicode__(self):
        return "%s la %s" % (self.prueba, self.fecha)

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta)
    descripcion = models.TextField()    
    orden = models.IntegerField ()
    puntaje = models.IntegerField()

    def __unicode__(self):
        return "%s en %s" % (self.orden, self.pregunta)

class Seleccion(models.Model):
    prueba_contestada = models.ForeignKey(PruebaContestada)
    respuesta = models.ForeignKey(Respuesta)

    def __unicode__(self):
        return "%s la %s" % (self.prueba_contestada, self.respuesta)

