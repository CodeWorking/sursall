from django.contrib import admin
from models import *
from encuestas.models import Persona


class SeleccionAdmin(admin.ModelAdmin):
    list_display = ('respuesta', 'pregunta')
    search_fields = ('pregunta',)
    list_filter = ('pregunta__seccion',)



admin.site.register(Persona)
admin.site.register(Prueba)
admin.site.register(Modulo)
admin.site.register(Seccion)
admin.site.register(Pregunta)
admin.site.register(SeccionContestada)
admin.site.register(Respuesta)
admin.site.register(Seleccion, SeleccionAdmin)

