"""webtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render, redirect

from  .views import *


urlpatterns = [

    url(r'^user_role_fun/', user_role_fun,name="user_role_fun"),
    url(r'^user_role_operation/([^/]+)/',  user_role_operation,name="user_role_operation"),
    #url(r'^user_role_operation/([^/]+)/',  RolesPagerView.as_view(),name="RolesPagerView"),
    url(r'^user_user_fun/', user_user_fun,name="user_user_fun"),
    url(r'^user_user_operation/([^/]+)/',  user_user_operation,name="user_user_operation"),
    url(r'^user_password_reset/',  user_password_reset,name="user_password_reset"),
    url(r'^sys_user_role/query',  sys_user_role_query,name="sys_user_role_query"),
]