from django.urls import re_path as url
from AliquotaApp import views

urlpatterns = [
    url(r'^produto$', views.produtoApi),
    url(r'^produto/([0-9]+)$', views.produtoApi)
]