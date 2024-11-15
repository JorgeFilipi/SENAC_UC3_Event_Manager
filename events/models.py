from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    start_time = models.TimeField(null=True, blank=True)
    end_date = models.DateTimeField()
    end_time = models.TimeField(null=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=300)

    def __str__(self):
        return f"Evento: {self.name} - Início: {self.start_date} {self.start_time} - Término: {self.end_date} {self.end_time} - Descrição: {self.description} - Local: {self.location}"


class Inscricao(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=200)
    participant_email = models.EmailField()
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'participant_email')
