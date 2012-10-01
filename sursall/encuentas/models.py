from django.db import models

class Usuario(models.Model):
    id_usuario = models.CharField(unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=75)
    contrasena = models.CharField(max_length=10)
    
class Persona(models.Model):
    id_persona = models.CharField(unique=True)
    edad = models.CharField(max_length=3)
    apellido = models.CharField(max_length=50)
    tipo_usuario = models.CharField(max_length=50)
    
class Prueba_contestada(models.Model):
    id_prieba_contestada = models.CharField(unique=True)  
    id_prueba = models.ForeignKey(Prueba)
    fecha = models.DateField() 
    hora = models.DateTimeField()
    
class Prueba(models.Model):
    id_prueba = models.CharField(unique=True)
    nombre = models.CharField(max_length=50)

class Modulo(models.Model):  
    id_modulo = models.CharField(unique=True)
    nombre = models.CharField(max_length=50)

class Seccion(models.Model):
    id_seccion = models.CharField(unique=True)
    instruccion = models.CharField(max_length=50)

class Pregunta(models.Model):
    id_pregunta = models.CharField(unique=True)
    descripcion_text = models.TextField()
    descripcion_imag = models.ImageField(upload_to='imagen', verbose_name='imagen')
    tiempo = models.DateTimeField()
    tipo_pregunta = models.CharField(max_length=20)
    
class Respuesta(models.Model):
    id_respuesta = models.CharField(unique=True)
    descripcion = models.TextField()    
    O_correcta = models.IntegerField()
    orden = models.IntegerField()
    puntaje = models.IntegerField()
    
class Seleccion(models.Model):
    id_prueba_contestada = models.ForeignKey(Prueba_contestada)
    id_respuesta = models.ForeignKey(Respuesta)
    