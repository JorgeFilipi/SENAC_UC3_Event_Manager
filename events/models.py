from django.db import models
from django.contrib.auth.models import User



class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateTimeField()
    end_time = models.TimeField(null=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=300)
    organizador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Evento: {self.name} - Início: {self.start_date} {self.start_time} - Término: {self.end_date} {self.end_time} - Descrição: {self.description} - Local: {self.location}"


class Inscricao(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Enveto: {self.event.name} - Participante: {self.usuario} - E-mail: {self.usuario.email} - Hora: {self.registration_date}"
