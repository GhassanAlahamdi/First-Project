import imp
from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
# Create your views here.



def hello(request: HttpResponse):

    phrase : str = "Hello World, This is my new HOME !"
    
    return HttpResponse(phrase)