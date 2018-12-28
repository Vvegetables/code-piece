#django 1.10 之后版本
import json

from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls.base import reverse

from django_test import settings
from django.contrib.auth.decorators import login_required


class SaveUserInfoMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
 
    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # 调用 view 之前的代码
        if isinstance(request.user,AnonymousUser) and getattr(settings,"DEBUG",True):
#             user = User.objects.get(id=5)
            request.user = None

        path = request.path_info
        if not ("login" in path):
            if len(path.split("/")) > 2:
                user = request.user
#                     logout(user)
                if not user.is_authenticated():
#                         return HttpResponse(json.dumps({"state":1,"data":"请先登录！"}),content_type="application/json")
#                         return redirect("/users/mylogin")
                    return HttpResponseRedirect("/")


         
        if request.body:
            try:
                req_body = json.loads(request.body)
                if req_body.get("sid"):
                    user.defaultsubject = req_body.get("sid")
                if req_body.get("range"):
                    user.defaultyear = ",".join(req_body.get("range",""))
                    user.save()
            except:
                pass

        response = self.get_response(request)
 
        # Code to be executed for each request/response after
        # the view is called.
        # 调用 view 之后的代码
 
        return response
    
    
    