from django import forms
from .models import Assignment
from django.contrib.auth.models import User



class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['file']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
