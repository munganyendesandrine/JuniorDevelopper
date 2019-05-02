from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404

def index(request):
    return render(request,"index.html")
    

def content_of_day(request):

    # content = content.todays_content () 
    return render(request, 'all-content/today-content.html')

def lesson1(request):
     return render(request,"lesson1.html")

