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
    # url(r'^admin/', admin.site.urls),
    # url(r'^login/', login),
    # url(r'^index/', index),
    url(r'^login/', login),
    # url(r'^index/', index),
    # url(r'^head/', head,name="web_head"),
    # url(r'^left/', left,name="web_left"),
    # url(r'^main/', main,name="web_main"),
    # url(r'^grid_query/', grid_query,name="grid_query"),

]