from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('modules/', views.module_list, name='module_list'),
    path('enroll/<int:module_id>/', views.enroll, name='enroll'),
    path('modules/<int:module_id>/', views.module_detail, name='module_detail'),
    path('modules/<int:module_id>/submit/', views.submit_assignment, name='submit_assignment'),
    path('trainer/dashboard/', views.trainer_dashboard, name='trainer_dashboard'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
