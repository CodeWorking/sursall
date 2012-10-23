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
                       url(r'^prueba(?P<id_prueba>\d+)/$', 'prueba'),
                       )        
