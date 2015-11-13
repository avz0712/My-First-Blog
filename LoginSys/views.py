# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.core.context_processors import csrf
# from django.contrib.auth.forms import UserCreationForm
from Blog.forms import UserCreationForm

__author__ = 'Anrew Zaharovskyi'


# Create your views here.


def login(request):
    arg = {}
    arg.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            arg['login_error'] = 'User not found'
            return render_to_response('LoginSys/login.html', arg)
    else:
        return render_to_response('LoginSys/login.html', arg)


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    arg = {}
    arg.update(csrf(request))
    arg['form'] = UserCreationForm()
    if request.POST:
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'],
                                         password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/')
        else:
            arg['form'] = new_user_form
    return render_to_response('LoginSys/register.html', arg)
