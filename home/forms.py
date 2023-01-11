from django import forms
from .models import feedback
from django.forms import ModelForm

class Taskform(ModelForm):
    class Meta:
        model = feedback
        fields = ('name','email','phone','desc')
