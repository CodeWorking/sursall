from django.contrib import admin
from models import *
from encuestas.models import Persona


admin.site.register(Persona)
admin.site.register(Prueba)
admin.site.register(Modulo)
admin.site.register(Seccion)
admin.site.register(Pregunta)
admin.site.register(PruebaContestada)
admin.site.register(Respuesta)
admin.site.register(Seleccion)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name')
    search_fields = ('first_name', 'last_name')
