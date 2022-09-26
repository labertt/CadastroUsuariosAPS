from django.db import models
from django.contrib.auth.models import User
from validacao.validators import validacao_cpf, validacao_nome, validacao_email

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=256, validators=[validacao_nome])
    cpf = models.IntegerField(validators=[validacao_cpf])
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=256)
    email = models.CharField(max_length=256, validators=[validacao_email])
    password = models.CharField(max_length=20)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nome_completo