from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #if request.method =="GET":
    #   return HttpResponse("hello world!")
    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)