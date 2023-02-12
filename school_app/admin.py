from django.contrib import admin
from .models import Teacher, Form, Subject, Student, TeachersSubject


class TeacherAdmin(admin.ModelAdmin):
    list_display = 'name', 'surname', 'homeform_teacher'


class FormAdmin(admin.ModelAdmin):
    list_display = 'name', 'homeform_teacher'


class SubjectAdmin(admin.ModelAdmin):
    pass


class StudentAdmin(admin.ModelAdmin):
    list_display = 'name', 'surname', 'form'


class TeachersSubjectsAdmin(admin.ModelAdmin):
    list_display = 'subject', 'teacher', 'form'


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(TeachersSubject, TeachersSubjectsAdmin)
