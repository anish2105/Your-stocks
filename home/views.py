from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def feedback(request):
    return render(request,'feedback.html')
