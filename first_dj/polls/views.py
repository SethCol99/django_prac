from django.shortcuts import render
from django.http import HttpResponse

#from . import urls 

# Create your views here.
def index(request):
    return HttpResponse("Hello there, this is the polls index")
