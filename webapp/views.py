from django.shortcuts import render, redirect
import socket


# Create your views here.


def index(request):
     if request.session.get('username',default=None):
         return render(request, 'main/index.html')
     else:
         return render(request, 'login/login.html')

def page_not_found(request):
    return render(request, '404.html')

#500页面
def page_error(request):
    return render(request, '500.html')

#403页面
def permission_denied(request):
    return render(request, '403.html')

