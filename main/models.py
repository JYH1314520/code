from django.db import models

# Create your models here.


class newsList(models.Model):
    newsId  =  models.AutoField(primary_key=True)
    newsName = models.CharField(max_length=200, unique=True,db_index=True)
    newsAuthor =  models.CharField(max_length=200,null=True,blank=True)
    newsStatus = models.CharField(max_length=200,null=True,blank=True)
    newsLook = models.CharField(max_length=200,null=True,blank=True)
    isShow = models.CharField(max_length=200,null=True,blank=True)
    newsTime  = models.DateField(null=True,blank=True)

