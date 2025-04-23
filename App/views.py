from django.shortcuts import render, redirect
from .models import Module, Enrollment, Student
from django.contrib.auth.decorators import login_required
from .forms import AssignmentForm 


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

@login_required
def submit_assignment(request, module_id):
    student = Student.objects.get(user=request.user)
    module = Module.objects.get(id=module_id)

    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.module = module
            assignment.student = student
            assignment.save()
            return redirect('module_list')
    else:
        form = AssignmentForm()

    return render(request, 'submit_assignment.html', {'form': form, 'module': module})