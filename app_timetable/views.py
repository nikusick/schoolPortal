from django.http import JsonResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Event
from .utils import Calendar


# Create your views here.
def timetable(request, year, month):
    c = Calendar(year, month)
    context = {
        "calendar": mark_safe(c.formatmonth()),
    }
    print(c.formatmonth())
    return render(request, 'timetable.html', context)


# Display all events.
def all_events(request):
    all_events = Event.objects.all()
    out = []
    for event in all_events:
        out.append({
            'title': event.title,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S")})
    return JsonResponse(out, safe=False)


# Create event.
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Event(title=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


# Update event.
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.start = start
    event.end = end
    event.title = title
    event.save()
    data = {}
    return JsonResponse(data)


# Remove event.
def remove(request):
    id = request.GET.get("id", None)
    event = Event.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)
