# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('encuestas.views',
                       url(r'^$', 'autenticacion'),
                       url(r'^usuario/nuevo$','nuevousuario'),
                       url(r'^ingresar/$','ingresar'),
                       )



