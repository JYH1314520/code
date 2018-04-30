from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import datetime
from .models import *
import  json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.db import connection,transaction


import hashlib
from django.contrib.auth.hashers import make_password



def runquery(sql):
    cursor = connection.cursor()
    cursor.execute(sql,None)
    col_names = [desc[0] for desc in cursor.description]
    row=cursor.fetchone()
    row = dict(zip(col_names, row))
    return row

# Create your views here.

def userfun(request):
    return render(request, 'user/user.html')

def getuserlist(request):
    lists = []
    userLists = User.objects.all()
    for rec in userLists:
        try:
            start_date = datetime.strftime(rec.start_date, '%Y-%m-%d')
        except:
            start_date = ' '

        list = {"rows":[{'user_id': rec.user_id, 'user_name': rec.user_name}],
                "total":1,
                "success":True
                }

        lists.append(list)
    return HttpResponse(json.dumps(list))


def user_role_fun(request):
    return render(request, 'user/user_role.html')


def user_user_fun(request):
    return render(request, 'user/user_user.html')


def user_role_operation(request,operation):
     if operation == 'query':
                            lists = []
                            role_code = request.GET.get('role_code')
                            role_name = request.GET.get('role_name')
                            roledescription = request.GET.get('role_description')
                            kwargs = {}
                            if role_code is not None:
                                kwargs['role_code'] = role_code
                            if role_name is not None:
                                kwargs['role_name'] = role_name
                            if roledescription is not None:
                                kwargs['roledescription'] = roledescription
                            roleLists = role.objects.filter(**kwargs )
                            paginator = Paginator(roleLists, request.GET.get('pagesize'))  # Show 25 contacts per page
                            page = request.GET.get('page')
                            try:
                                contacts = paginator.page(page)
                            except PageNotAnInteger:
                                # If page is not an integer, deliver first page.
                                contacts = paginator.page(1)
                            except EmptyPage:
                                # If page is out of range (e.g. 9999), deliver last page of results.
                                contacts = paginator.page(paginator.num_pages)
                            rows =[]
                            for rec in contacts:
                                try:
                                    start_date = datetime.strftime(rec.start_date, '%Y-%m-%d')
                                except:
                                    start_date = ' '
                                try:
                                    end_date = datetime.strftime(rec.end_date, '%Y-%m-%d')
                                except:
                                    end_date = ' '
                                try:
                                    rows.append({'role_id': rec.role_id,
                                                 'role_code': rec.role_code,
                                                 'role_name': rec.role_name,
                                                 'start_date': start_date,
                                                 'end_date': end_date,
                                                 'roledescription' :rec.roledescription,
                                                 'enable_flag':rec.enable_flag})
                                except:
                                    rows.append({})

                            list = {"rows":rows,
                                    "total":roleLists.count(),
                                    "success":True
                            }
                            lists.append(list)
                            return HttpResponse(json.dumps(list))
     if operation == 'insert':
                                   if 'POST' == request.method:
                                     data = request.body
                                     datajson = json.loads(data)
                                     heigh = 0
                                     querysetlist = []
                                     for item in datajson:
                                         heigh = heigh +1
                                         b = role(role_code = item['role_code'],
                                         role_name =  item['role_name'],
                                         start_date =  item['start_date'],
                                         end_date = item['end_date'],
                                         enable_flag = item['enable_flag'],
                                         roledescription = item['roledescription'])
                                         b.save()
                                         item['role_id'] = b.role_id
                                         querysetlist.append(item)
                                     list = {"rows": querysetlist, "total": heigh, "success": True,"message":'cheng'}
                                     return HttpResponse(json.dumps(list))
     if operation == 'remove':
         if 'POST' == request.method:
             data = request.body
             datajson = json.loads(data)
             for item in datajson:
                 role_id = item['role_id']
                 role.objects.filter(role_id=role_id).delete()
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
            p = role.objects.get(role_id=role_id)
            p.role_name = role_name
            p.start_date = start_date
            p.roledescription = roledescription
            p.enable_flag = enable_flag
            p.end_date = end_date
            p.save()  # 保存
        return HttpResponse(data)



def user_user_operation(request,operation):
     if operation == 'query':
                            lists = []
                            user_name = request.GET.get('user_name')
                            employee_code = request.GET.get('employee_code')
                            employee_name = request.GET.get('employee_name')
                            status = request.GET.get('status')
                            kwargs = {}
                            if user_name is not None:
                                kwargs['user_name'] = user_name
                            if employee_code is not None:
                                kwargs['employee_code'] = employee_code
                            if employee_name is not None:
                                kwargs['employee_name'] = employee_name
                            if status is not None:
                                kwargs['status'] = status
                            userLists = User.objects.filter(**kwargs ).order_by('user_name')
                            paginator = Paginator(userLists, request.GET.get('pagesize'))  # Show 25 contacts per page
                            page = request.GET.get('page')
                            try:
                                contacts = paginator.page(page)
                            except PageNotAnInteger:
                                # If page is not an integer, deliver first page.
                                contacts = paginator.page(1)
                            except EmptyPage:
                                # If page is out of range (e.g. 9999), deliver last page of results.
                                contacts = paginator.page(paginator.num_pages)
                            rows =[]
                            # print('query')
                            for rec in contacts:
                                try:
                                    start_date = datetime.strftime(rec.start_date, '%Y-%m-%d')
                                except:
                                    start_date = ' '
                                try:
                                    end_date = datetime.strftime(rec.end_date, '%Y-%m-%d')
                                except:
                                    end_date = ' '
                                try:
                                    rows.append({'user_id': rec.user_id,
                                                 'user_name': rec.user_name,
                                                 'description': rec.description,
                                                 'start_date': start_date,
                                                 'end_date': end_date,
                                                 'email':rec.email, 'phone': rec.phone,
                                                 'status' :rec.status,
                                                 'enable_flag':rec.enable_flag})
                                except:
                                    rows.append({})

                            list = {"rows":rows,
                                        "total":userLists.count(),
                                        "success":True
                            }
                            return HttpResponse(json.dumps(list))
     if operation == 'insert':
         if 'POST' == request.method:
             data = request.body
             datajson = json.loads(data)
             heigh = 0
             querysetlist = []
             for item in datajson:
                 heigh = heigh + 1
                 b = User(user_name=item['user_name'],
                          email=item['email'],
                          phone=item['phone'],
                          start_date=item['start_date'],
                          end_date=item['end_date'],
                          status=item['status'],
                          description=item['description'])
                 b.save()
                 item['user_id'] = b.user_id
                 querysetlist.append(item)
             list = {"rows": querysetlist, "total": heigh, "success": True}
             return HttpResponse(json.dumps(list))
     if operation == 'remove':
         if 'POST' == request.method:
             data = request.body
             datajson = json.loads(data)
             for item in datajson:
                 user_id = item['user_id']
                 User.objects.filter(user_id=user_id).delete()
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
            print(start_date)
            p = role.objects.get(role_id=role_id)
            p.role_name = role_name
            p.start_date = start_date
            p.roledescription = roledescription
            p.enable_flag = enable_flag
            p.end_date = end_date
            p.save()  # 保存

        return HttpResponse(data)

def user_password_reset(request):
     if 'POST' == request.method:
         user_id =  request.POST['user_id']
         print(user_id)
         password = request.POST['password']
         md5password =  make_password(password, None, 'pbkdf2_sha256') #hashlib.md5(password.encode("utf-8"))
         p = User.objects.get(user_id=user_id)
         p.password_encrypted = md5password
         p.save()
         list = {"rows": {}, "total": 1, "success": True}
     return HttpResponse(json.dumps(list))




