from django.urls import path
from . import views

urlpatterns = [
    path('', views.taskList, name = 'taskList'),
    path('create/', views.taskCreate, name = 'taskCreate'),
    path('<int:pk>/update/', views.taskUpdate, name = 'taskUpdate'),
    path('<int:pk>/delete', views.taskDelete, name = 'taskDelete'),
]
