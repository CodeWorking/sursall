from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('encuestas.views',
                       url(r'^$', 'ingresar'),
                       url(r'^usuario/nuevo$','nuevousuario'),
                       url(r'^bienvenido$','bienvenido'),
                       url(r'^nuevousuario$','nuevousuario'),
                       url(r'^contacto/$','contacto'),
                       url(r'^base/$','base'),    
                       url(r'^prueba/(?P<id_prueba>\d+)/', 'prueba')                     
                       )        