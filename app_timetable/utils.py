from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event, Timetable, Term


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, weekday):
        term = Term.objects.filter(start__lte=day, stop__gte=day)
        d = ''
        if term:
            sub_per_day = Timetable.objects.filter(term=term[0].id, day__name=weekday)
            for subject in sub_per_day:
                d += f'<li>{subject.subject.name}</li>'
        return f"<td><details><summary>{day}</summary><p><ul> {d} </ul></p></details></td>"

    # formats a week as a tr
    def formatweek(self, week):
        _week = ''
        for day in week:
            _week += self.formatday(day, week.index(day))
        return f'<tr> {_week} </tr>'

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        it = cal.find(str(self.year)) + len(str(self.year))
        cal = cal[:it] + '<input type="month" onchange="goTo(this.value)">' + cal[it:]
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdatescalendar(self.year, self.month):
            cal += f'{self.formatweek(week)}\n'
        return cal
