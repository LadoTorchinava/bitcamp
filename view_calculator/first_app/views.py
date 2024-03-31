from django.shortcuts import render
from django.http import HttpResponse

def index(request, number):
    if number % 2 == 0:
        return HttpResponse("this number is even")
    else:
        return HttpResponse("this number is odd")