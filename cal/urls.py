from django.urls import path
from . import views




urlpatterns = [
    path('', views.conversion, name="conversion"),
    path('result', views.result, name="result"),
    path('about/', views.about, name="about"),
]