from django.db import models
from aluno.models import Aluno
from validacao.validators import validator_data_presenca

class Presenca(models.Model):
    nome_aluno_presenca = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_presenca = models.DateField(validators=[validator_data_presenca])
    presente = models.BooleanField()

    def __str__(self) -> str:
        return self.nome_aluno_presenca