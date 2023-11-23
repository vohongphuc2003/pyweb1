from django.shortcuts import render
from django.http import HttpResponse

def trangchu(request) :
    return render(request , 'web1/trangchu.html')
def base(request) :
    return render(request , 'web1/base.html')
