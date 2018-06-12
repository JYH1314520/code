from django.http import HttpResponse
from django.shortcuts import render, redirect
from   django.template.loader import get_template
from user.models import User
import cgi
import cgitb; cgitb.enable()


# Create your views here.


def index(request):
     if request.user.is_authenticated == True:
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

#获取页面路由
def html_get(request,operation1,operation2):
    context = request.GET
    # for i in arguments.keys():
    #     print( arguments[i].value)
    return render(request, operation1 +"/"+ operation2+".html" ,context)

