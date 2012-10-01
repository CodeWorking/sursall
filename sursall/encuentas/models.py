from django.db import models


class Persona(models.Model):
    edad = models.CharField(max_length=3)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    usuario = models.ForeignKey("auth.User")


class Prueba(models.Model):
    nombre = models.CharField(max_length=50)


class Modulo(models.Model):  
    nombre = models.CharField(max_length=50)


class Seccion(models.Model):
    instruccion = models.CharField(max_length=50)


class Pregunta(models.Model):
    descripcion_text = models.TextField()
    descripcion_imag = models.ImageField(upload_to='imagen')
    tiempo = models.IntegerField()
    tipo_pregunta = models.CharField(max_length=20)


class PruebaContestada(models.Model):
    id_prieba_contestada = models.CharField(unique=True)  
    id_prueba = models.ForeignKey(Prueba)
    fecha = models.DateField() 
    hora = models.DateTimeField()


class Respuesta(models.Model):
    descripcion = models.TextField()    
    O_correcta = models.IntegerField()
    orden = models.IntegerField()
    puntaje = models.IntegerField()


class Seleccion(models.Model):
    id_prueba_contestada = models.ForeignKey(Prueba_contestada)
    id_respuesta = models.ForeignKey(Respuesta)

