from django.contrib import admin
from .models import Classroom, ClassroomFreedom, FormFreedom, Lesson, TeacherFreedom, Timetable, Event, Term, Day


class ClassroomAdmin(admin.ModelAdmin):
    pass


class ClassroomFreedomAdmin(admin.ModelAdmin):
    pass


class FormFreedomAdmin(admin.ModelAdmin):
    pass


class LessonAdmin(admin.ModelAdmin):
    pass


class TeacherFreedomAdmin(admin.ModelAdmin):
    pass


class TimetableAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


class TermAdmin(admin.ModelAdmin):
    pass


class DayAdmin(admin.ModelAdmin):
    pass


admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(ClassroomFreedom, ClassroomFreedomAdmin)
admin.site.register(FormFreedom, FormFreedomAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(TeacherFreedom, TeacherFreedomAdmin)
admin.site.register(Timetable, TimetableAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Day, DayAdmin)