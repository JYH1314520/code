from django.db import models




# Create your models here.
class function(models.Model):
    function_id = models.AutoField(primary_key=True,db_index=True,unique=True)
    function_code = models.CharField(max_length=50,db_index=True,unique=True)
    function_name = models.TextField(max_length=2000,blank=True)
    title  = models.TextField(max_length=2000)
    parent_function_id = models.ForeignKey('self', related_name='function',on_delete=models.CASCADE,  blank=True)
    href = models.CharField(max_length=1000,blank=True)
    icon = models.TextField(max_length=2000,blank=True)
    spread = models.BooleanField(blank=True)
    url = models.URLField(blank=True)
    function_type = models.CharField(max_length=50,blank=True)
    enable_flag = models.CharField(max_length=1,blank=True)
    def __unicode__(self):
        return self.function_code







