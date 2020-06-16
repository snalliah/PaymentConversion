from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *

from .forms import CreateUserForm, MemberForm

#from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

#from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

#from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')


            messages.success(request, 'Account was created for ' + username)

            return redirect('login')


    context = {'form':form}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user.is_superuser:
            return redirect('http://127.0.0.1:8000/admin')
        else:
            if user is not None:
                login(request, user)
                return redirect('profileUpdate')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return redirect('login')
    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def memberPage(request, mem_id):
    member = Member.objects.get(id=mem_id)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'profileUpdate', context)
    else:
        return redirect('home')
    return render(request, 'accounts/member.html', context)

def profileUpdate(request):
    member = request.user.member
    form = MemberForm(instance=member)

    if request.method == 'POST':
        form = MemberForm(request.POST, requst.FILES,instance=member)
        if form.is_valid():
            form.save()



    context = {'form':form}
    return render(request, 'accounts/profileUpdate.html', context)