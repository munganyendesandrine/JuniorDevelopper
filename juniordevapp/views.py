from django.shortcuts import render,redirect

from django.http import HttpResponse, Http404,HttpResponseRedirect
# import pygame
# Create your views here.
def welcome(request):

    return render(request,'welcome.html')
def game(request):
   
    return render(request,'games.html')