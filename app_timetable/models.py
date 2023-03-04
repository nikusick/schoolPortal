import datetime
import time

from django.db import models
from django.urls import reverse

from app_school.models import Teacher, Form, Subject


class Classroom(models.Model):
    number = models.CharField(max_length=10)
    seating = models.PositiveIntegerField()

    def __str__(self):
        return self.number


class Day(models.Model):
    DAY_CHOICE = {
        (0, 'понедельник'),
        (1, 'вторник'),
        (2, 'среда'),
        (3, 'четверг'),
        (4, 'пятница'),
        (5, 'суббота'),
        (6, 'воскресенье')
    }
    name = models.IntegerField(max_length=1, choices=DAY_CHOICE)

    def __str__(self):
        return self.name


class Term(models.Model):
    start = models.DateField()
    stop = models.DateField()


class Lesson(models.Model):
    start = models.TimeField()
    stop = models.TimeField()

    def __str__(self):
        return f'{self.start} - {self.stop}'


class FormFreedom(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=False)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)


class ClassroomFreedom(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=False)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)


class TeacherFreedom(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)


class Timetable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


class Event(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return self.title
