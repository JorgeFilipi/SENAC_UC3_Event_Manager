from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm, InscricaoForm
from .models import Event, Inscricao


def index(request):
    return render(request, 'index.html')


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    inscricoes = Inscricao.objects.filter(event=event)
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.event = event
            inscricao.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = InscricaoForm()

    return render(request, 'events/event_detail.html', {'event': event, 'form': form, 'inscricoes': inscricoes})


def event_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_add.html', {'form': form})


def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_delete.html', {'event': event})
