from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def create_function():
     return  None

def function_operation(request,operation):
     list = {"rows": [{"functionId":12,"moduleCode":"122","functionCode":"12122"}], "total": 1, "success": True}
     return  HttpResponse(json.dumps(list))

def functionset(request):
     return  render(request,"fnd/sys_function.html")
