from django.contrib import admin
from django.urls import path,include
from . import views 


urlpatterns = [
    path('',views.trangchu, name='Home'),
    path('/1', views.base, name='base')
]
