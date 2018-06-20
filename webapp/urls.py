"""webapp URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

from webapp.settings import NEVER_REDIS_TIMEOUT
from .views import *
from user.models import *
from django.core.cache import cache
from fnd.models import fnd_prompts
from webapp.basefun import *








urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name="web_index"),
    url('^login/', include('login.urls')),
    url('^main/', include('main.urls')),
    url('^user/', include('user.urls')),
    url('^fnd/', include('fnd.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^([^/]+)/([^/]+).html/$', html_get, name="html_get"),
]

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error


def cache_prompts_all():
    a_lists = fnd_prompts.objects.filter(lang="zh-cn")
    print('初始化将查询到的数据加载到缓存中')
    rows =  []
    for list in a_lists:
        row = {"code":list.prompt_code,"value":list.description}
        rows.append(row)
    cache.set("fnd_prompts_all",rows)


def     cache_prompts():
         a_lists = fnd_prompts.objects.filter(lang="zh-cn")
         print('初始化将查询到的数据加载到缓存中')
         rows = []
         #row =  convert_to_dicts(a_list)
         for list in a_lists:
             cache.set('fnd_prompts'+list.prompt_code, list.description,NEVER_REDIS_TIMEOUT)
             row = {"code": list.prompt_code, "value": list.description}
             rows.append(row)
         cache.set("fnd_prompts_all", rows,NEVER_REDIS_TIMEOUT)
cache_prompts()

#cache_prompts_all


