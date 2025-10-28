from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tasks(models.Model):
    user =  models.ForeignKey(User , on_delete = models.CASCADE)
    task_name = models.CharField(max_length = 150)
    task_dec = models.TextField(max_length = 300   , default='Description not provided by the developer......')
    task_code = models.TextField(max_length = 10000 , default='Code not provided by the developer......')
    task_date = models.DateTimeField(auto_now_add = True)
    task_updated = models.DateTimeField(auto_now = True)
    task_pic = models.ImageField(upload_to = 'pics/' , blank = True , null = True)

    def __str__(self):
        return f' {self.user.username} - {self.task_name}'

