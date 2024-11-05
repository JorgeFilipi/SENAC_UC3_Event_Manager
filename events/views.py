from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm
from .models import Event


def index(request):
    return render(request, 'index.html')


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


def event_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            print("Formulário salvo com sucesso!")
            return redirect('event_list')
        else:
            print("Formulário inválido:", form.errors)
    else:
        form = EventForm()
    return render(request, 'events/event_add.html', {'form': form})