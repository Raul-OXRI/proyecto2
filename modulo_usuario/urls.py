from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('singup/', views.singup, name='singup'),
    path('login/', views.login_view, name='login'),
    path('list_users/', views.list_users, name='list_users'),
    path('edit_role/<int:user_id>/', views.edit, name='edit'),
]