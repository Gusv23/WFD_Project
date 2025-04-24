from django.db import models
from django.contrib.auth.models import User

class Module(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="modules")

    def __str__(self):
        return self.title

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} → {self.module}"

class Material(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.module.title})"
    
class Assignment(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='assignments')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignments/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.student} → {self.module}"
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender} to {self.recipient}"

