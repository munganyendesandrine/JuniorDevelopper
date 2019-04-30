from django.shortcuts import render,redirect
from django.http  import HttpResponse

def content(request):
    return render(request, 'content.html')

def content_of_day(request):
    return render(request, 'content.html')