from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.register, name='register'),
    path('calculator', views.calculator, name='calculator'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
