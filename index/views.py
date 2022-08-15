from django.shortcuts import render,redirect
from . import views
from .models import stocks
from .forms import Taskform
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.

@login_required
def stockpage(request):
    # log_user = request.user
    stock = stocks.objects.filter(user = request.user)

    return render(request,'stockindex.html' , {'stock':stock})

def addstock(request):
    submitted = False
    if request.method == "POST":
        form = Taskform(request.POST or None)

        if form.is_valid():

            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect('?submitted = True')
    else:
        form = Taskform
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'addstock.html',{'form':form,'submitted':submitted} )



def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        stock = stocks.objects.filter(nameofstocks__contains = searched)
        return render(request,'search.html' , {'searched':searched , 'stock':stock})
    else:
        return render(request,'search.html' , {'searched':searched , 'stock':stock})

def stats(request):
    return render(request,'stats.html')

def update(request,update_id):
    stock = stocks.objects.get(pk = update_id)
    form = Taskform(request.POST or None , instance  = stock)  #this is for auto filling the update form
    if form.is_valid():
        form.save()
    return render(request,'update.html',{'stock':stock})

def delete(request,delete_id):
    stock = stocks.objects.get(pk = delete_id)
    stock.delete()
    return redirect('stockpage')
