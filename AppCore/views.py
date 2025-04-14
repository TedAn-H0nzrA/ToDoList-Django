from django.shortcuts import render

def welcome(request):
    return render(request, 'Core/welcome.html')

def home(request):
    return render(request, 'Core/home.html')