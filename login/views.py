
from django.http import HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, redirect

from django.views import generic

from django.contrib.auth.hashers import make_password, check_password
from django.views.decorators.csrf import csrf_exempt

from .models import  function
import hashlib
from django.core.serializers import serialize
from user.models import User









class LoginView(generic.ListView):
    template_name = 'login/login.html'
    context_object_name = 'login_info_list'

    def get_queryset(self):
        return " "



@csrf_exempt
def login(request):

    if request.method == "POST":
        data =  request.body;
        user_name = request.POST['username']
        passwd =    request.POST['passwd']
        try:
         loginuser =  User.objects.filter(user_name=user_name)
         print(loginuser[0].password_encrypted)
        except :
            return render(request, "login/login.html", {"error_msg": "no such user"})

        if check_password(passwd, loginuser[0].password_encrypted):
        # if hashlib.md5(passwd) ==  loginuser[0].password_encrypted:
              request.session['user_id'] = loginuser[0].user_id
              request.session['username'] = loginuser[0].user_name
              #return render(request, 'main/index.html', {"session":request.session})
              return redirect("/")
        else:
             print('234433')
             return render(request, "login/login.html", {"error_msg": "用户名或密码错误"})



def head(request):
    return render(request, 'login/head.html', {"request":request})

def left(request):
    function_data = function.objects.filter(parent_function_id=None)
    return render(request, 'login/left.html', {"function":function_data})

def main(request):

    return render(request, 'login/main.html')

def user(request):

    return render(request, 'login/user.html')

def function_url(request,nid):
    html =     function.objects.get(function_id=nid).function_url
     # return render(request, html)
     # html = 'app001/user.html'
    return render(request, html)




def grid_query(request):

    # build a config suitable to pass to jqgrid constructor
    resp = function.objects.all()
    return HttpResponse(serialize('json', resp), content_type="application/json")

