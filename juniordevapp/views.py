from django.shortcuts import render
from .models import Teacher,Student,Parent,School
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def teacher(request,id):
    email = Teacher.objects.get(e_mail)

    return render(request,'teach.html')