from django.db import models
from aluno.models import Aluno
from validacao.validators import validator_data_pagamento

class Pagamento(models.Model):
    meses = (
        ('Janeiro', 'Janeiro'),
        ('Feveiro', 'Feveiro'),
        ('Março', 'Março'),
        ('Abril', 'Abril'),
        ('Maio', 'Maio'),
        ('Junho', 'Junho'),
        ('Julho', 'Julho'),
        ('Agosto', 'Agosto'),
        ('Setembro', 'Setembro'),
        ('Outubro', 'Outubro'),
        ('Novembro', 'Novembro'),
        ('Dezembro', 'Dezembro')
    )

    pagamentos = (
        ('Dinheiro', 'Dinheiro'),
        ('Cartão de Crédito/Débito', 'Cartão de Crédito/Débito'),
        ('Pix', 'Pix')
    )


    nome_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_pagamento = models.DateField(validators=[validator_data_pagamento])
    mes_pagamento = models.CharField(max_length=256, blank=False, null=True, choices=meses)
    forma_pagamento = models.CharField(max_length=256, blank=False, null=True, choices=pagamentos)
    valor_pagamento = models.CharField(max_length=30, blank=False, null=True)


    def __str__(self) -> str:
        return self.nome_aluno