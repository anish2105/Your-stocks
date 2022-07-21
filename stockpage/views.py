from django.shortcuts import render
from . import views
from .models import stocks
# Create your views here.
def stockpage(request):
    stock = stocks.objects.all()
    return render(request,'stockindex.html' , {'stock':stock})

def addstock(request):
    
    return render(request,'addstock.html')

def stats(request):
    return render(request,'stats.html')
