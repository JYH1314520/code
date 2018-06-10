from django.db import models




# Create your models here.
class function(models.Model):
    function_id = models.AutoField(primary_key=True,db_index=True,unique=True)
    function_code = models.CharField(max_length=50,db_index=True,unique=True)
    function_name = models.TextField(max_length=2000,blank=True)
    function_description  = models.TextField(max_length=2000)
    sequence = models.BigIntegerField(null=True,blank=True)
    parent_function_id = models.ForeignKey('self',null=True,blank=True,on_delete=models.CASCADE)
    href = models.CharField(max_length=1000,blank=True)
    icon = models.TextField(max_length=2000,blank=True)
    spread = models.NullBooleanField(blank=True,null=True,default=False)
    url = models.URLField(blank=True)
    function_type = models.CharField(max_length=50,blank=True)
    enable_flag = models.CharField(max_length=1,blank=True)

    class Meta:
        db_table="fnd_function"
    def __unicode__(self):
        return self.function_code

class fnd_prompts(models.Model):
    prompt_id  = models.AutoField(primary_key=True)
    prompt_code = models.CharField(max_length=240)
    lang  = models.CharField(max_length=40)
    description = models.TextField(max_length=2000,null=True,blank=True)
    enable_flag =  models.CharField(max_length=1,blank=True)
    status = models.CharField(max_length=30, null=True,blank=True)
    created_by = models.IntegerField(default=1)
    creation_date = models.DateField(auto_now_add=True)
    last_updated_by = models.IntegerField(default=1)
    last_update_date = models.DateField(auto_now=True)
    attribute_category = models.CharField(max_length=30, null=True,blank=True)
    attribute1 = models.CharField(max_length=240, null=True,blank=True)
    attribute2 = models.CharField(max_length=240, null=True,blank=True)
    attribute3 = models.CharField(max_length=240, null=True,blank=True)
    attribute4 = models.CharField(max_length=240, null=True,blank=True)
    attribute5 = models.CharField(max_length=240, null=True,blank=True)
    attribute6 = models.CharField(max_length=240, null=True,blank=True)
    attribute7 = models.CharField(max_length=240, null=True,blank=True)
    attribute8 = models.CharField(max_length=240, null=True,blank=True)
    attribute9 = models.CharField(max_length=240, null=True,blank=True)
    attribute10 = models.CharField(max_length=240, null=True,blank=True)
    attribute11 = models.CharField(max_length=240, null=True,blank=True)
    attribute12 = models.CharField(max_length=240, null=True,blank=True)
    attribute13 = models.CharField(max_length=240, null=True,blank=True)
    attribute14 = models.CharField(max_length=240, null=True,blank=True)
    attribute15 = models.CharField(max_length=240, null=True,blank=True)
    request_id = models.IntegerField(null=True,blank=True)
    program_id = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table="fnd_prompts"
        unique_together = ('prompt_code', 'lang')


    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))








