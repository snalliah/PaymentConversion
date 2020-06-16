from django.urls import path
from . import views


urlpatterns = [
   
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('member/<str:mem_id>/', views.memberPage, name="member"),
    path('profile/', views.profileUpdate, name="profileUpdate"),
]