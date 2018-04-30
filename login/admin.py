from django.contrib import admin

# Register your models here.
from .models import  function,sys_user

admin.site.register(function)
admin.site.register(sys_user)