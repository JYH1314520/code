from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, name, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(username=name,
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):

        user = self.create_user(name, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id  =  models.AutoField(primary_key=True)
    username = models.CharField('用户',max_length=200, unique=True,db_index=True)
    user_type = models.CharField('用户类型',max_length=200,null=True, db_index=True)
    password_encrypted =  models.CharField(max_length=200)
    email = models.EmailField('邮箱',max_length=255,null=True, unique=True, db_index=True)
    phone = models.CharField(max_length=20, null=True)
    enable_flag = models.CharField(max_length=1,blank=True)
    bg_admin_flag  = models.CharField(max_length=1,null=True,blank=True)
    company_id = models.IntegerField(null=True,blank=True)
    employee_id = models.IntegerField(null=True,blank=True)
    frozen_flag  = models.CharField('冻结',max_length=1,null=True,blank=True)
    start_date  = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    status  = models.CharField(max_length=30,null=True,blank=True)
    created_by =  models.IntegerField(default=1)
    creation_date = models.DateField(auto_now_add=True)
    last_updated_by =  models.IntegerField(default=1)
    last_update_date = models.DateField(auto_now=True)
    attribute_category =  models.CharField(max_length=30,null=True,blank=True)
    attribute1         =  models.CharField(max_length=240,null=True,blank=True)
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
    last_login_date = models.DateField(null=True,blank=True)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    access_token = models.CharField(max_length=100, blank=True)
    refresh_token = models.CharField(max_length=100, blank=True)
    last_password_update_date = models.DateField(null=True,blank=True)
    first_login =  models.CharField(max_length=1,null=True,blank=True)
    description = models.CharField(max_length=255, null=True,blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    employee_id =  models.IntegerField(null=True,blank=True)
    customer_id = models.IntegerField(null=True,blank=True)
    vendor_id =  models.IntegerField(null=True,blank=True)
    request_id = models.IntegerField(null=True,blank=True)
    program_id = models.IntegerField(null=True,blank=True)
    is_superuser = models.BooleanField(default=True)
    last_login   = models.DateTimeField(null=True,blank=True)
    date_joined  =models.DateTimeField(null=True,blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        ordering = ('-creation_date',)
        db_table = "sys_user"

    def __unicode__(self):
        return self.username

    def get_full_name(self):
        return self.description

    def get_short_name(self):
        return self.description

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin



    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class role(models.Model):
    role_id  = models.AutoField(primary_key=True)
    role_code = models.CharField(help_text='角色代码',max_length=200, unique=True,db_index=True)
    role_name = models.CharField(help_text='角色名称',max_length=240, null=True,blank=True)
    roledescription = models.CharField(max_length=2000, null=True,blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
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
        db_table="sys_role"

    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class sys_user_role(models.Model):
    sur_id  = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=True,blank=True)
    role_id  = models.IntegerField(null=True,blank=True)
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
        db_table="sys_user_role"


    def toJSON(self):
        import json
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))



