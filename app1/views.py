from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    return HttpResponse("This is app 1")
def index1(request) :
    return HttpResponse("This is app's child 1")
