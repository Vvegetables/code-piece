#coding=utf-8
from django.conf.urls import url

from self_application import views
from django.views.generic.base import TemplateView


app_name="self_template_define"

urlpatterns = [
    url(r"^hello/",views.hello),
    url(r"^login/",views.login), 
]