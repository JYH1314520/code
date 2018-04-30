from django.db import models
from django.contrib import admin



# Create your models here.

class function(models.Model):
    function_id = models.AutoField(primary_key=True)
    function_code = models.CharField(max_length=50)
    function_name = models.TextField(max_length=2000)
    parent_function_id = models.ForeignKey('self', related_name='function',on_delete=models.CASCADE, null=True, blank=True)
    function_url = models.CharField(max_length=1000,blank=True)
    url = models.URLField(blank=True)
    function_type = models.CharField(max_length=50,blank=True)
    enable_flag = models.CharField(max_length=1,blank=True)
    def __unicode__(self):
        return self.function_code




class sys_role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_code = models.CharField(max_length=50)
    role_name = models.TextField(max_length=2000)
    enable_flag = models.CharField(max_length=1,blank=True,default='N')



class sys_user(models.Model):
    user_id  =  models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200, unique=True,db_index=True)
    password =  models.CharField(max_length=200)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    enable_flag = models.CharField(max_length=1,blank=True)
    bg_admin_flag  = models.CharField(max_length=1,null=True)
    company_id = models.IntegerField(null=True)
    employee_id = models.IntegerField(null=True)
    frozen_flag  = models.CharField(max_length=1,null=True)
    start_date  = models.DateField(null=True)
    end_date = models.DateField(null=True)



