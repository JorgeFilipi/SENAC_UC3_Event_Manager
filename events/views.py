from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm, InscricaoForm, RegistroUsuario
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
        form = InscricaoForm(request.POST, event=event)
        if form.is_valid():
            inscricao = form.save(commit=False)
            inscricao.event = event
            inscricao.save()
            assunto = 'Confirmação de Inscrição no Evento'
            mensagem = f'Você se inscreveu com sucesso no evento {event.name}.'
            enviar_email(inscricao.participant_email, assunto, mensagem)
            return redirect('event_detail', event_id=event.id)

    else:
        form = InscricaoForm()

    return render(request, 'events/event_detail.html', {'event': event, 'form': form, 'inscricoes': inscricoes})


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


def editar_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, id=id)
    if request.method == 'POST':
        form = InscricaoForm(request.POST, instance=inscricao)
        if form.is_valid():
            form.save()
            assunto = 'Confirmação de Atualização de Inscrição'
            mensagem = f'Sua inscrição no evento {inscricao.event.name} foi atualizada com sucesso.'
            enviar_email(inscricao.email, assunto, mensagem)
            return redirect('event_detail', event_id=inscricao.event.id)
    else:
        form = InscricaoForm(instance=inscricao)

    return render(request, 'events/event_edit_inscription.html', {'form': form, 'inscricao': inscricao})


def delete_inscricao(request, id):
    inscricao = get_object_or_404(Inscricao, id=id)
    if request.method == 'POST':
        inscricao.delete()
        assunto = 'Confirmação de Cancelamento de Inscrição'
        mensagem = f'Sua inscrição no evento {inscricao.event.name} foi cancelada com sucesso.'
        enviar_email(inscricao.email, assunto, mensagem)
        return redirect('event_detail', event_id=inscricao.event.id)
    return render(request, 'events/event_delete_inscription.html', {'inscricao': inscricao})


def enviar_email(destinatario, assunto, mensagem):
    send_mail(
        assunto,
        mensagem,
        settings.EMAIL_HOST_USER,
        [destinatario],
        fail_silently=False,
    )


@login_required
def inscrit_add(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    inscricoes = Inscricao.objects.filter(event=event)
    return render(request, 'events/inscrit_add.html', {'inscricoes': inscricoes})
