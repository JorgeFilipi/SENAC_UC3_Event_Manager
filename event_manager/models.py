from django.db import models

class  Evento(models.Model):
    nome = models.CharField(max_length=100)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    descricao = models.TextField()
    localizacao = models.TextField(max_length=100)

    def __str__(self):
        return self.nome
