from django.db import models
from django.contrib.auth.models import Group, User
import django


# Create your models here.

class System(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    profile_pic = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.first_name

class Tag(System):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        ordering = []    
 

class User(models.Model):
    title = models.TextField(null=False, blank=False)
    status = models.CharField(default='inactive', max_length=10)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)




class Profile(models.Model):
    user = models.OneToOneField(django.contrib.auth.models.User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, null=False, blank=False)
    salary = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('-salary',)

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.designation)
    
    
# class CustomDjangoModelPermission(permissions.DjangoModelPermissions):
    
#     def __init__(self):
#         self.perms_map = copy.deepcopy(self.perms_map)  # from EunChong's answer
#         self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']   

class CustomGroup(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=8)
    
    def __str__(self):
        return "{}".format(self.group.name)
        
    group = models.OneToOneField('auth.Group', unique=True, on_delete=models.CASCADE)  

