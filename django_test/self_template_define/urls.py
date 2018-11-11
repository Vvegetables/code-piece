#coding=utf-8
from django.conf.urls import url

from self_template_define import views
from django.views.generic.base import TemplateView


app_name="self_template_define"

urlpatterns = [
    url(r"^index/",TemplateView.as_view(template_name="index.html")) 
]