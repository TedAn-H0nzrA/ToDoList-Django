from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from .models import User

# Register views
def registerViews(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            user.save()
    else:
        form = RegisterForm()

    return render(request, 'Auth/register.html', {'form' : form})

# Login views
def loginViews(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email = email).first()

            if user and user.check_password(password):
                login(request, user)

    else:
        form = LoginForm()

    return render(request, 'Auth/login.html', {'form' : form})

# Logout
def logoutViews(request):
    logout(request)
    return redirect(login)