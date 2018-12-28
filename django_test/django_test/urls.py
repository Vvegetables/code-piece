"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import celery_task


urlpatterns = [
    
    url(r'^chat/', include('websocket_chat_test.urls')),
    url(r'^admin/', admin.site.urls),
    url(r"^template/",include("self_template_define.urls",namespace="self_template_define")),
    url(r"^app/",include("self_application.urls",namespace="self_application")),
    url(r"^do/$",celery_task.views.do),
]
