from django import forms
from .models import stocks
from django.forms import ModelForm

class Taskform(ModelForm):
    class Meta:
        model = stocks
        fields = ('nameofstocks','buy','buydate','sell','selldate','t1','t2')
