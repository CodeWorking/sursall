from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('encuestas.views',
                       url(r'^$', 'ingresar'),
                       url(r'^usuario/nuevo$','nuevousuario'),
                       url(r'^bienvenido$','bienvenido'),
                       )