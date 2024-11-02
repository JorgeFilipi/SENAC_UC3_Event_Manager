from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    location = models.CharField(max_length=300)

    def __str__(self):
        return self. f"Evento: {self.name} - Inicio: {self.start_date} - ternino: {self.end_date} - Descrição: {self.description} - Local: {self.location}"