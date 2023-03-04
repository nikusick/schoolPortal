from django.shortcuts import render
from django.views import View, generic
from .models import Student, TeachersSubject, Form


class StudentView(generic.DetailView):
    model = Student
    template_name = '../templates/app_school/student_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context


class TeacherView(generic.DetailView):
    model = Student
    template_name = '../templates/app_school/teacher_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = TeachersSubject.objects.only('subject__name').filter(teacher=self.object.id).all()
        return context


class FormView(generic.DetailView):
    model = Form
    template_name = '../templates/app_school/form_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.only('name', 'surname').filter(form=self.object.id).all()
        return context
