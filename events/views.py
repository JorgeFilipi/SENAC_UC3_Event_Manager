from django.shortcuts import render

import events
from .models import Event
from django.shortcuts import get_object_or_404


def event_list(request):
    query = Event.objects.all()
    nome = request.GET.get('nome')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    description = request.GET.get('description')
    location = request.GET.get('location')

    return render(request, 'events/event_list.html', {'events': events})

