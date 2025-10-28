from django import forms
from .models import tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class task_from(forms.ModelForm):
    class Meta:
        model = tasks
        fields = ['task_pic' , 'task_name' , 'task_dec' ,  'task_code']


class new_user_form(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1', 'password2')