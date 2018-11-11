from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Task(models.Model):
    name = CharField("姓名",max_length=500,null=True,blank=True)
    age = IntegerField("年龄",null=True,blank=True)
    sex = IntegerField("性别",choices=(('男',0),("女",1)),default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "t_bd_task"
        verbose_name_plural = "任务"
        
