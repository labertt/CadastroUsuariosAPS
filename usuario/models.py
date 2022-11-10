from django.db import models
from django.contrib.auth.models import User
from validacao.validators import validacao_cpf, validacao_nome, validacao_email, validacao_endereco, validator_data, validator_sem_nums

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=256, validators=[validacao_nome, validator_sem_nums])
    cpf = models.IntegerField(unique=True, validators=[validacao_cpf])
    data_nascimento = models.DateField(validators=[validator_data])
    endereco = models.CharField(max_length=256, validators=[validacao_endereco])
    email = models.CharField(unique=True, max_length=256, validators=[validacao_email])
    usernome = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return self.nome_completo