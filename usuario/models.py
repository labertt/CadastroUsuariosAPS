from django.db import models
from django.contrib.auth.models import User
from validacao.validators import validacao_cpf, validacao_nome, validacao_email, validacao_endereco, validacao_password

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=256, validators=[validacao_nome])
    cpf = models.IntegerField(unique=True, validators=[validacao_cpf])
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=256, validators=[validacao_endereco])
    email = models.CharField(unique=True, max_length=256, validators=[validacao_email])
    password = models.CharField(unique=True, max_length=20, validators=[validacao_password])
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nome_completo