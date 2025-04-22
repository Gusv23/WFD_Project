from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('modules/', views.module_list, name='module_list'),
]
