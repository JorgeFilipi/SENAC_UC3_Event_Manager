from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from events.forms import EdicaoUsuario, RegistroUsuario
from events.models import Inscricao, Event


def dashboard(request):
    inscricao = Inscricao.objects.filter(usuario=request.user)
    eventos = Event.objects.filter(organizador=request.user)
    lista_inscricoes = Inscricao.objects.filter(event_detalhe__organizador=request.user)
    lista_eventos = Event.objects.all()
    total_inscricoes = Inscricao.objects.filter(detalhes_evento__organizador=request.user).count()

    return render(request, "users/dashboard.html",
                  {'inscricao': inscricao, 'eventos': eventos, 'lista_inscricoes': lista_inscricoes,
                   'lista_eventos': lista_eventos, 'total_inscricoes': total_inscricoes})


@login_required
def editar_usuario(request):
    usuario_atual = request.user.first_name
    if request.method == "POST":
        form = EdicaoUsuario(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request, 'registration/editar_usuario.html', {'form': form, 'usuario': usuario_atual})
    else:
        form = EdicaoUsuario(instance=request.user)

        return render(request, 'registration/editar_usuario.html', {'form': form})


def register_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuario()
    return render(request, 'registration/register.html', {'form': form})
