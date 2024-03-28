from django.http import HttpResponse

def index(request):
    return HttpResponse("empty page")

def home(request):
    return HttpResponse("this is home page")

def about(request):
    return HttpResponse("this is about page")

def contact(request):
    return HttpResponse("this is contact page")