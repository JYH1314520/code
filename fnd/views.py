from django.shortcuts import render
from django.http import HttpResponse
import json
from  .models import function,fnd_prompts
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from webapp.basefun import *
# Create your views here.

def create_function():
     return  None

def function_operation(request,operation):
     if operation == 'query':
          lists = []
          function_code = request.GET.get('function_code')
          function_name = request.GET.get('function_name')
          title = request.GET.get('title')
          kwargs = {}
          if function_code is not None:
               kwargs['function_code'] = function_code
          if function_name is not None:
               kwargs['function_name'] = function_name
          if title is not None:
               kwargs['title'] = title
          functionLists = function.objects.filter(**kwargs)
          paginator = Paginator(functionLists, request.GET.get('pagesize'))  # Show 25 contacts per page
          page = request.GET.get('page')
          try:
               contacts = paginator.page(page)
          except PageNotAnInteger:
               # If page is not an integer, deliver first page.
               contacts = paginator.page(1)
          except EmptyPage:
               # If page is out of range (e.g. 9999), deliver last page of results.
               contacts = paginator.page(paginator.num_pages)
          rows = []
          for rec in contacts:
               #try:
                    rows.append({'function_id': rec.function_id, 'function_code': rec.function_code, 'function_name': rec.function_name,
                                 'parent_function_id': rec.parent_function_id, 'href': rec.href,'icon': rec.icon,
                                 'spread': rec.spread, 'url': rec.url,'function_type': rec.function_type,
                                 'enable_flag': rec.enable_flag})
               # except:
               #      rows.append({})

          list = {"rows": rows, "total": functionLists.count(), "success": True}
          lists.append(list)
          return HttpResponse(json.dumps(list))
     if operation == 'insert':
          if 'POST' == request.method:
               data = request.body
               datajson = json.loads(data)
               heigh = 0
               querysetlist = []
               for item in datajson:
                    heigh = heigh + 1
                    b = function(function_code=item['function_code'], function_name=item['function_name'], function_type=item['function_type'],
                                 parent_function_id=item['parent_function_id'],href =item['href'],
                                 function_description=item['function_description'],icon=item["icon"],sequence=item['sequence'])
                    b.save()
                    item['function_id'] = b.function_id
                    querysetlist.append(item)
               list = {"rows": querysetlist, "total": heigh, "success": True, "message": 'cheng'}
               return HttpResponse(json.dumps(list))
     if operation == 'remove':
          if 'POST' == request.method:
               data = request.body
               datajson = json.loads(data)
               for item in datajson:
                    function_id = item['function_id']
                    function.objects.filter(function_id=function_id).delete()
               return HttpResponse(data)

     if operation == 'submit':
          if 'POST' == request.method:
               data = request.body
               datajson = json.loads(data)
               heigh = 0
               rows = []
               for item in datajson:
                    function_id = item['function_id']
                    function_type = item['function_type']
                    function_name = item['function_name']
                    parent_function_id = item['parent_function_id']
                    icon = item['icon']
                    sequence = item['sequence']
                    title = item['title']
                    href = item['href']
                    function_description = item['function_description']
                    p = function.objects.get(function_id=function_id)
                    p.function_type = function_type
                    p.function_name = function_name
                    p.parent_function_id = parent_function_id
                    p.sequence = sequence
                    p.icon = icon
                    p.function_description = function_description
                    p.href = href
                    p.title = title
                    p.save()  # 保存
          return HttpResponse(data)
def functionset(request):
     return  render(request,"fnd/sys_function.html")


def fnd_prompt_operation(request, operation):
     if operation == 'query':
          lists = []
          prompt_code = request.GET.get('prompt_code')
          description = request.GET.get('description')
          lang = request.GET.get('lang')
          kwargs = {}
          if prompt_code is not None:
               kwargs['prompt_code'] = prompt_code
          if description is not None:
               kwargs['description'] = description
          if lang is not None:
               kwargs['title'] = lang
          fnd_promptsLists = fnd_prompts.objects.filter(**kwargs)
          paginator = Paginator(fnd_promptsLists, request.GET.get('pagesize'))  # Show 25 contacts per page
          page = request.GET.get('page')
          try:
               contacts = paginator.page(page)
          except PageNotAnInteger:
               # If page is not an integer, deliver first page.
               contacts = paginator.page(1)
          except EmptyPage:
               # If page is out of range (e.g. 9999), deliver last page of results.
               contacts = paginator.page(paginator.num_pages)
          rows = []
          for rec in contacts:
               try:
                    rows.append({'prompt_id': rec.prompt_id, 'prompt_code': rec.prompt_code,
                                 'lang': rec.lang, 'description': rec.description,
                                 'enable_flag': rec.enable_flag})
               except:
                    rows.append({})

          list = {"rows": rows, "total": fnd_promptsLists.count(), "success": True}
          lists.append(list)
          return HttpResponse(json.dumps(list))
     if operation == 'insert':
          if 'POST' == request.method:
               data = request.body
               datajson = json.loads(data)
               heigh = 0
               querysetlist = []
               for item in datajson:
                    heigh = heigh + 1
                    b = fnd_prompts(prompt_code=item['prompt_code'], lang=item['lang'], description=item['description'],enable_flag ="Y")
                    b.save()
                    item['prompt_id'] = b.prompt_id
                    querysetlist.append(item)
               list = {"rows": querysetlist, "total": heigh, "success": True, "message": 'cheng'}
               return HttpResponse(json.dumps(list))
     if operation == 'remove':
          if 'POST' == request.method:
               data = request.body
               datajson = json.loads(data)
               for item in datajson:
                    prompt_id = item['prompt_id']
                    fnd_prompts.objects.filter(prompt_id=prompt_id).delete()
               return HttpResponse(data)

     if operation == 'submit':
          if 'POST' == request.method:
               data = request.body
               datajson = json.loads(data)
               heigh = 0
               rows = []
               for item in datajson:
                    prompt_id = item['prompt_id']
                    prompt_code = item['prompt_code']
                    description = item['description']
                    lang = item['lang']
                    enable_flag = item['enable_flag']
                    p = fnd_prompts.objects.get(prompt_id=prompt_id)
                    p.prompt_code = prompt_code
                    p.description = description
                    p.lang = lang
                    p.enable_flag = enable_flag
                    p.save()  # 保存
          return HttpResponse(data)


def functionset(request):
     return render(request, "fnd/sys_function.html")


