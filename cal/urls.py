from django.urls import path
from . import views





urlpatterns = [
   
    path('', views.home, name="home"),
    path('conversion', views.conversion, name="conversion"),
    path('result', views.result, name="result"),
    path('about/', views.about, name="about"),
    path('test/', views.test, name="test"),
    path('navbar/', views.navbar, name="navbar"),
]