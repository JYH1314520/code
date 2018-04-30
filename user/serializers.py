from rest_framework import serializers
from .models import *
from rest_framework.pagination import PageNumberPagination



class MyPagination(PageNumberPagination):
    cursor_query_param = ('role_code')
    page_size = 20  #默认每页显示数据条数
    page_query_param = "page"  #第几页参数，在url中设置
    page_size_query_param = "pagesize" #定制每页显示的数据条数的参数，在url中设置

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = role
        fields = ( 'role_id','role_code', 'role_name', 'roledescription','start_date','end_date','enable_flag','status')


