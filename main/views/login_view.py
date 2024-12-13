from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import logout
from django.contrib import messages

def logout_user(request):
    logout(request)
    messages.info(request, 'Deslogado com sucesso.')
    return redirect('main:home')