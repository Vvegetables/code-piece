from django.db import models

class TeacherResume(models.Model):
    teachername = models.CharField("教师名字", max_length=255, null=True, blank=True)
    telephone = models.CharField("电话", max_length=255, null=True, blank=True)
    email = models.CharField("邮箱", max_length=255, null=True, blank=True)
    research_direction = models.CharField("研究方向", max_length=500, null=True, blank=True)
    personal_profile = models.TextField("个人简介", null=True, blank=True)
    teaching_results = models.TextField("教学成果", null=True, blank=True)
    research_results = models.TextField("研究结果", null=True, blank=True)
    lab_introduction = models.TextField("实验室介绍", null=True, blank=True)
    
    def __str__(self):
        return self.teachername
    
    class Meta:
        db_table = "t_tt_teacherresume"

