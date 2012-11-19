from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('encuestas.views',
                       url(r'^$', 'ingresar'),
                       url(r'^ingresar$', 'ingresar'),
                       url(r'^contacto/$', 'contacto'),
                       url(r'^base/$', 'base'),
                       url(r'^administrador/$', 'administrador'),
                       url(r'^logoutuser/$', 'logoutuser'),
                       url(r'^DevContacto/$', 'DevContacto'),
                       url(r'^contestar_prueba/(?P<id_prueba>\d+)/$', 'prueba'),
                       url(r'^contestar_seccion/(?P<id_seccion>\d+)/$', 'seccion'),
                       url(r'^contestar_modulo/(?P<id_modulo>\d+)/$', 'modulo'),
                       url(r'^contestar_pregunta/(?P<id_pregunta>\d+)/$', 'pregunta'),
                       url(r'^contestar_respuesta/(?P<id_respuesta>\d+)/$', 'respuesta'),
                       url(r'^ver_resultados/$', 'resultados'),
                       url(r'^resultados/(?P<id_usuario>\d+)/$', 'gestionresultados'),
                       url(r'^seccion_contestada_resultados/(?P<id_sec_cont>\d+)/$', 'seccion_contestada_resultados'),
                       url(r'^estudiante/$', 'estudiante'),
                       )        