from django.shortcuts import render
from django.http import HttpResponse

def index(request, name):
    return HttpResponse(f"hello {name}")
