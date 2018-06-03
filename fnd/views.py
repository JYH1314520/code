from django.shortcuts import render
from django.http import HttpResponse
import json
from  .models import function
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
               try:
                    rows.append({'function_id': rec.function_id, 'function_code': rec.function_code, 'function_name': rec.function_name,
                                 'title': rec.title, 'parent_function_id': rec.parent_function_id, 'href': rec.href,'icon': rec.icon,
                                 'spread': rec.spread, 'url': rec.url,'function_type': rec.function_type,
                                 'enable_flag': rec.enable_flag})
               except:
                    rows.append({})

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
                    role_id = item['role_id']
                    function.objects.filter(role_id=role_id).delete()
               return HttpResponse(data)

     if operation == 'submit':
          if 'POST' == request.method:
               data = request.body
               datajson = json.loads(data)
               heigh = 0
               rows = []
               for item in datajson:
                    role_id = role_id = item['role_id']
                    role_name = item['role_name']
                    start_date = item['start_date']
                    end_date = item['end_date']
                    enable_flag = item['enable_flag']
                    roledescription = item['roledescription']
                    p = function.objects.get(role_id=role_id)
                    p.role_name = role_name
                    p.start_date = start_date
                    p.roledescription = roledescription
                    p.enable_flag = enable_flag
                    p.end_date = end_date
                    p.save()  # 保存
          return HttpResponse(data)
def functionset(request):
     return  render(request,"fnd/sys_function.html")


