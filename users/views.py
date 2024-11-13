from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from events.forms import EdicaoUsuario
from events.models import Inscricao, Event


# Create your views here.
def dashboard(request):
    inscricao = Inscricao.objects.filter(usuario=request.user)
    eventos = Event.objects.filter(organizador=request.user)

    return render(request, "users/dashboard.html", {'inscricao': inscricao, 'eventos': eventos})

@login_required
def editar_usuario(request):
    if request.method == "POST":
        form = EdicaoUsuario(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        return render(request, 'registration/editar_usuario.html', {'form': form})
    else:
        form = EdicaoUsuario(instance=request.user)

        return render(request, 'registration/editar_usuario.html', {'form': form})

