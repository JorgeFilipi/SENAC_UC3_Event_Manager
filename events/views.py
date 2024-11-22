from django.conf import settings
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .forms import EventForm, RegistroUsuario
from .models import Event, Inscricao


def index(request):
    return render(request, 'index.html')


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detalhe(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    inscricoes = Inscricao.objects.filter(event_id=event_id)
    return render(request, 'events/event_detalhe.html', {'event': event, 'inscricoes': inscricoes})


def inscrit_add(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if Inscricao.objects.filter(usuario=request.user, event=event).exists():
        messages.error(request, 'Você já está inscrito neste evento.')
        return redirect('event_detalhe', event_id)

    if request.method == 'POST':
        inscricao = Inscricao.objects.create(
            usuario=request.user,
            event=event,
            registration_date=datetime.now(),
        )
        inscricao.save()
        messages.success(request, 'Inscrição realizada com sucesso!')
        return redirect('event_detalhe', event.id)

    return render(request, 'events/inscrit_add.html', {'event': event})


@login_required
def event_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/event_add.html', {'form': form})


@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_delete.html', {'event': event})


def register_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_eventos')
    else:
        form = RegistroUsuario()
    return render(request, 'registration/register.html', {'form': form})


def delete_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, id=id)
    if request.method == 'POST':
        inscricao.delete()
        return redirect('event_detalhe', event_id=inscricao.event.id)
    return render(request, 'events/event_delete_inscription.html', {'inscricao': inscricao})


def enviar_email(destinatario, assunto, mensagem):
    send_mail(
        assunto,
        mensagem,
        settings.EMAIL_HOST_USER,
        [destinatario],
        fail_silently=False,
    )
