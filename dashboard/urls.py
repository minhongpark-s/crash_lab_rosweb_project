from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('roslibjs', views.roslibjs, name='roslibjs'),
    path('roslibjsmain', views.roslibjsmain, name='roslibjsmain'),
    path('roslibjsSP', views.roslibjsSP, name='roslibjsSP'),
    path('serviceConnectionTest', views.serviceConnectionTest, name='serviceConnectionTest'),
]