from django.shortcuts import render
from .models import Module

def home(request):
    return render(request, 'home.html')

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'module_list.html', {'modules': modules})
