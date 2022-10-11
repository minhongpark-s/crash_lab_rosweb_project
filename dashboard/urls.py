from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('roslibjs', views.roslibjs, name='roslibjs'),
    path('roslibjsmain', views.roslibjsmain, name='roslibjsmain'),
]