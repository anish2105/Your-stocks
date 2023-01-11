from django.shortcuts import render,redirect
from . import views
from .models import stocks
from .forms import Taskform
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Avg, Count, Min, Sum
# Create your views here.

@login_required
def stockpage(request):
    # log_user = request.user
    stock = stocks.objects.filter(user = request.user)
    # data = stocks.objects.filter(user = request.user).aggregate(value =Sum('buy'))
    return render(request,'stockindex.html' , {'stock':stock }) #,'data':data

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
        stock = stocks.objects.filter(nameofstocks__contains = searched , user = request.user)
        return render(request,'search.html' , {'searched':searched , 'stock':stock})
    else:
        return render(request,'search.html' , {'searched':searched , 'stock':stock})

def stats(request):
    stock = stocks.objects.filter(user = request.user)
    t_buy = stocks.objects.filter(user = request.user).aggregate(value =Sum('buy'))
    t_sell = stocks.objects.filter(user = request.user).aggregate(value =Sum('sell'))
    winnings = stocks.objects.filter(user = request.user).aggregate(Sum('buy'), Sum('sell'))
    profit =   winnings["sell__sum"] - winnings["buy__sum"]

    return render(request,'stats.html',  {'t_buy':t_buy ,'t_sell':t_sell , 'stock':stock , 'profit' : profit})

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
