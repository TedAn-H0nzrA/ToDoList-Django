from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerViews, name = 'register'),
    path('login/', views.loginViews, name = 'login'),
    path('logout/', views.logoutViews, name = 'logout'),
]