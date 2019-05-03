from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404

def index(request):
    return render(request,"index.html")
    

def content_of_day(request):

    # content = content.todays_content () 
    return render(request, 'all-content/today-content.html')

def lesson2(request):
     return render(request,"lesson2.html")

def lesson3(request):
     return render(request,"lesson3.html")


def lesson4(request):
     return render(request,"lesson4.html")


def lesson5(request):
     return render(request,"lesson5.html")

# def viewallpages(request):
#      return render(request,"viewallpages.html")

def quizlesson2(request):
     return render(request,"quizlesson2.html")


