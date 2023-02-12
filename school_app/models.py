from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    homeform_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.surname


class Form(models.Model):
    name = models.CharField(max_length=3)
    homeform_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth_date = models.DateField()
    GENDER_CHOICE = {
        ('м', 'мужской'),
        ('ж', 'женский')
    }
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)

    photo = models.FileField(upload_to='images/students/', default=None)

    form = models.ForeignKey(Form, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} {self.surname} ({self.form})'


class TeachersSubject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject} ({self.teacher})'


class Grade(models.Model):
    grade = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    description = models.TextField(default=None)



