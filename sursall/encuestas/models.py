from django.db import models


CHOICES_TIPO_PREGUNTA = ((0,"Una pregunta"),)

class Persona(models.Model):
    edad = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.ForeignKey("auth.User")


class Prueba(models.Model):
    nombre = models.CharField(max_length=50)
    

class Modulo(models.Model):  
    nombre = models.CharField(max_length=50)
    prueba = models.ForeignKey(Prueba)
    
class Seccion(models.Model):
    instruccion = models.TextField()
    modulo = models.ForeignKey(Modulo)

class Pregunta(models.Model):
    descripcion_text = models.TextField()
    #descripcion_imag = models.ImageField(upload_to='imagen')
    tiempo = models.IntegerField(null=True, blank=True)
    tipo_pregunta = models.IntegerField(choices=CHOICES_TIPO_PREGUNTA)
    seccion = models.ForeignKey(Seccion)


class PruebaContestada(models.Model):
    prueba = models.ForeignKey(Prueba)
    fecha = models.DateTimeField()


class Respuesta(models.Model):
    descripcion = models.TextField()    
    O_correcta = models.IntegerField()
    orden = models.IntegerField ()
    puntaje = models.IntegerField()


class Seleccion(models.Model):
    prueba_contestada = models.ForeignKey(PruebaContestada)
    

