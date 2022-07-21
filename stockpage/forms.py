from django import forms
from .models import stocks

class Taskform(forms.ModelForm):
    class Meta:
        model = stocks
        fields = '__all__'
