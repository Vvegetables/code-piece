from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    realname = models.CharField("真实姓名",max_length=255,null=True,blank=True)
    
    class Meta(AbstractUser.Meta):
        db_table = "users"
