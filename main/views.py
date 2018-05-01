from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import newsList
import  json
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt



def main(request):

    return render(request, 'main/main.html')


def getpagenewslist(request):
    newsId = request.GET.get('newsId')
    newsdata = newsList.objects.filter(newsId=newsId)
    return render(request, 'main/page/news/newsEdit.html',{'newsdata': newsdata})

def systemParameter(request):

    data_dic = {"cmsName": "layui后台管理模版", "version": "1.0.0", "author": "请叫我宗威哥", "homePage": "page/index.html",
        "server": "windows", "dataBase": "8.00.2039", "maxUpload": "2M", "userRights": "总管理员",
        "description": "这是宗威哥闲来无事做的一套基于layui的cms模版，纯静态页面，不包含数据库", "powerby": "copyright @2017 请叫我宗威哥",
        "record": "京ICP备14040xxx号-1", "keywords": "layui，宗威哥，cms，模版"}


    return HttpResponse(json.dumps(data_dic))

def getnewsList(request):
    lists = []
    newsLists = newsList.objects.all()
    for rec in newsLists:
                            try:
                               newsTime =  datetime.strftime(rec.newsTime, '%Y-%m-%d')
                            except:
                               newsTime = ' '

                            list = {
                                'newsId' : rec.newsId,
                                'newsName': rec.newsName,
                                'newsAuthor': rec.newsAuthor,
                                'newsStatus': rec.newsStatus,
                                'newsLook': rec.newsLook,
                                'isShow': rec.isShow,
                                'newsTime':newsTime
                            }

                            lists.append(list)

    return HttpResponse(json.dumps(lists))

@csrf_exempt
def savenewsList(request):
 if 'POST' == request.method:
    data = request.POST
    for item in request.POST:
        newsName = eval(item).get('newsName')
        newsAuthor = eval(item).get('newsAuthor')
        newsStatus = eval(item).get('newsStatus')
        newsLook = eval(item).get('newsLook')
        isShow = eval(item).get('isShow')
        newsTime =  eval(item).get('newsTime')
    print(newsName)
    print(newsLook)
    try:

        newsList.objects.create(newsName=newsName,
                                newsAuthor=newsAuthor,
                                newsStatus=newsStatus,
                                newsLook=newsLook,
                                isShow=isShow,
                                newsTime = newsTime
                               )
    except:

        result = [{'_status': 'fail'}]
    else:
        result = [{'_status': 'success'}]

    return   HttpResponse(data)

def deletenewsList(request):
    if 'POST' == request.method:
     try:
      data = request.POST
      print(data)
      newsId = request.POST.get('newsId')
      print(newsId)
      newsList.objects.filter(newsId = newsId).delete()
     except:

         result = [{'_status': 'fail'}]
     else:
         result = [{'_status': 'success'}]


    return   HttpResponse(json.dumps(result))


def getfunction(request):

    data_dic = {
	"title" : "首页",
	"icon" : "icon-computer",
	"href" : "/static/main/page/main.html",
	"spread" : False
   },{
	"title" : "系统设置",
	"icon" : "&#xe614;",
	"href" : "",
	"spread" : False,
	"children" : [
		{
			"title" : "系统角色",
			"icon" : "&#xe613;",
			"href" : "/user/user_role_fun/",
			"spread" : False
		}, {"title": "系统用户",
            "icon": "&#xe613;",
            "href": "/user/user_user_fun/",
            "spread": False},
        {"title": "功能定义",
         "icon": "&#xe613;",
         "href": "/fnd/functionset/",
         "spread": False},
		{
			"title" : "二级菜单2",
			"icon" : "&#xe631;",
			"href" : "",
			"spread" : False
		}
	]
}


    return HttpResponse(json.dumps(data_dic))



def csrf_failure(request, reason):
    return render(request,'403.html')





