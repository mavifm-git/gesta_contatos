# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from gestao_contato.api.resources import ContatoResource

v1_api = Api(api_name='v1')
v1_api.register(ContatoResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
]
