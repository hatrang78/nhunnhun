from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello")

def nhun2(request):
    print("truy cap")
    return HttpResponse("Day la nhun2")

def nhun4(request):
    return HttpResponse("Day la nhun4")