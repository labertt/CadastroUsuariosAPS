from django.db import models
from validacao.validators import validacao_nome, validacao_cpf, validacao_endereco, validator_data, validator_sem_nums

class Aluno(models.Model):

    artes_marciais = (
        ('Kung Fu', 'Kung Fu'),
        ('Karatê', 'Karatê'),
        ('Judô', 'Judô'),
        ('Jiu-Jitsu', 'Jiu-Jitsu'),
        ('Muay Thai', 'Muay Thai'),
        ('Taekwondo', 'Taekwondo')
    )

    turnos = (
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Tarde'),
        ('Noturno', 'Noturno')
    )

    nome_completo_aluno = models.CharField(max_length=256, validators=[validacao_nome, validator_sem_nums])
    cpf_aluno = models.CharField(unique=True, max_length=256, validators=[validacao_cpf])
    data_nascimento_aluno = models.DateField(validators=[validator_data])
    endereco_aluno = models.CharField(max_length=256, validators=[validacao_endereco])
    turno_aluno = models.CharField(max_length=256)
    arte_marcial_aluno = models.CharField(max_length=256, blank=False, null=True, choices=artes_marciais)

    def __str__(self) -> str:
        return str(self.nome_completo_aluno)