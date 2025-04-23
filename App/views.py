from django.shortcuts import render, redirect
from .models import Module, Enrollment, Student
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def module_list(request):
    modules = Module.objects.all()
    return render(request, 'module_list.html', {'modules': modules})

@login_required
def enroll(request, module_id):
    student = Student.objects.get(user=request.user)
    module = Module.objects.get(id=module_id)
    Enrollment.objects.get_or_create(student=student, module=module)
    return redirect('module_list')

def module_detail(request, module_id):
    module = Module.objects.get(id=module_id)
    materials = module.materials.all()
    return render(request, 'module_detail.html', {'module': module, 'materials': materials})
