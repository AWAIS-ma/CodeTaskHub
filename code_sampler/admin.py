from django.contrib import admin
from .models import tasks
# Register your models here.

class tasksadmin(admin.ModelAdmin):
    list_display = ['task_name' , 'user' , 'task_date']


admin.site.register(tasks , tasksadmin)