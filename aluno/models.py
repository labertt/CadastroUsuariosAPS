from django.db import models
from validacao.validators import validacao_nome, validacao_cpf, validacao_endereco

class Aluno(models.Model):
    nome_completo_aluno = models.CharField(max_length=256, validators=[validacao_nome])
    cpf_aluno = models.CharField(max_length=256, validators=[validacao_cpf])
    data_nascimento_aluno = models.DateField()
    endereco_aluno = models.CharField(max_length=256, validators=[validacao_endereco])
    turno_aluno = models.CharField(max_length=256)
    arte_marcial_aluno = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.nome_completo_aluno
        