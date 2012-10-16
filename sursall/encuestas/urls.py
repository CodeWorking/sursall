from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('encuestas.views',
                       url(r'^$', 'ingresar'),
                       url(r'^usuario/nuevo$','nuevousuario'),
                       url(r'^bienvenido$','bienvenido'),
                       url(r'^base$','base'),
                       #url(r'^contactenos$','contactenos'),
                       url(r'^contactenos/$','contacto'),                       
                       )        