from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import logout

class Login(View):
    pass

def logout_user(request):
    logout(request)
    return redirect('main:home')