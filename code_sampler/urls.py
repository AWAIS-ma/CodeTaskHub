from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.home , name = "home"),

    path('create/' , views.create_task , name = "create"),

    path('edit/<int:id>/' , views.edit , name = "edit"),

    path('delete_task/<int:id>/' , views.delete_task , name = "delete_task"),

    path('get_code/<int:id>/' , views.get_code , name = "get_code"),
    
    path('search/' , views.search , name = "search"),

    path('my_task/' , views.only_user_task , name = "my_task"),

    path('contact/' , views.contact , name = "contact"),

    path('register/' , views.user_reg , name = "new_user_registration"),


] 
