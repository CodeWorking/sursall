from django.contrib import admin
from models import *
from encuestas.models import Persona


class SeleccionAdmin(admin.ModelAdmin):
    list_display = ('respuesta', 'pregunta')
    search_fields = ('pregunta',)
    list_filter = ('pregunta__seccion',)
    #exclude = ['respuesta']

class PruebaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('tipo_usuario', 'usuario')
    search_fields = ('nombre', 'apellido')

class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'prueba')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('prueba__modulo',)

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'descripcion')
    search_fields = ('pregunta', 'descripcion')
    list_filter = ('pregunta__respuesta',)

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Prueba, PruebaAdmin)
admin.site.register(Modulo, ModuloAdmin)
admin.site.register(Seccion)
admin.site.register(Pregunta)
admin.site.register(SeccionContestada)
admin.site.register(Respuesta, RespuestaAdmin)
admin.site.register(Seleccion, SeleccionAdmin)
admin.site.register(competencia)
admin.site.register(competencia_seleccionada)

