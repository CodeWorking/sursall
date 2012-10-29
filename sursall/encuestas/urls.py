from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('encuestas.views',
                       url(r'^$', 'ingresar'),
                       url(r'^ingresar$', 'ingresar'),
                       url(r'^bienvenido$', 'bienvenido'),
                       url(r'^contacto/$', 'contacto'),
                       url(r'^base/$', 'base'),
                       url(r'^administrador/$', 'administrador'),
                       url(r'^logoutuser/$', 'logoutuser'),
                       url(r'^DevContacto/$', 'DevContacto'),
                       #url(r'^prueba(?P<id_prueba>\d+)/$', 'prueba'),
                       url(r'^pruebas/$','lista_pruebas'),
                       url(r'^prueba/(?P<id_prueba>\d+)$','detalle_prueba'),
                       url(r'^modulos/$','lista_modulos'),
                       url(r'^modulo/(?P<id_modulo>\d+)$','detalle_modulo'),
                       url(r'^secciones/$','lista_secciones'),
                       url(r'^seccion/(?P<id_seccion>\d+)$','detalle_seccion'),
                       )        
