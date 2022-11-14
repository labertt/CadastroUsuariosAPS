from django.db import models
from aluno.models import Aluno

class Pagamento(models.Model):
    nome_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_pagamento = models.DateField()

    def __str__(self) -> str:
        return self.nome_aluno