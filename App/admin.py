from django.contrib import admin
from .models import Module, Student, Enrollment, Material

admin.site.register(Module)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Material)
