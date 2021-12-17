from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.
def index(req):
    return render(req, 'login.html', {'title': 'Login'})


def do_login(req):
    username = req.POST['username']
    password = req.POST['password']

    user = authenticate(req, username=username, password=password)

    if user is not None:
        login(req, user)
        return redirect('/')
    else:
        messages.error(req, 'Username/password salah')
        return redirect('/login')


def do_logout(req):
    logout(req)
    return redirect('/')
