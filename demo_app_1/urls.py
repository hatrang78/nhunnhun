from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nhun2/', views.nhun2, name='nhun2'),
    path('nhun4/', views.nhun4, name='nhun4'),
]