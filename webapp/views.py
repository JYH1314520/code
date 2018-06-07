from django.http import HttpResponse
from django.shortcuts import render, redirect
import socket
from   django.template.loader import get_template
from user.models import User


# Create your views here.


def index(request):
     if request.session.get('username',default=None):
         _user_name = request.session.get('username')
         _template =  get_template("main/index.html")
         _user = User.objects.filter(username=_user_name)
         _userInfo = {
             "username":_user_name
         }
         _context = {_user
         }
         _output = _template.render(_userInfo)
         return HttpResponse(_output)
         # return render(request, 'main/index.html')
     else:
         return redirect("/login/")

def page_not_found(request):
    return render(request, '404.html')

#500页面
def page_error(request):
    return render(request, '500.html')

#403页面
def permission_denied(request):
    return render(request, '403.html')

