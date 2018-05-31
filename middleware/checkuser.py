from django.http import HttpResponse
from django.shortcuts import  redirect
import json
from django.utils.deprecation import MiddlewareMixin


class SimpleMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response
    def process_request(self,request,*args,**kwargs):

        if request.path_info == '/login/':
            return None
        if request.path_info == '/login/login/':
            return None
        userinfo = request.session.get('username', default=None)
        if not userinfo:
             return redirect('/login/')
    def process_response(self,request,response):
        return response