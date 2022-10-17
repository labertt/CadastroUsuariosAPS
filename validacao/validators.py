from django.core.exceptions import ValidationError 
from datetime import date

def validacao_cpf(value):
    if len(str(value)) != 11:
        raise ValidationError('O CPF tem que ter 11 dígitos!')
    else:
        return value

def validacao_nome(value):
    if len(value) < 3:
        raise ValidationError('O nome deve ter no mínimo 3 caracteres!')
    else:
        return value

def validacao_endereco(value):
    if len(value) < 5:
        raise ValidationError('O endereço deve ter no mínimo 5 caracteres!')
    else:
        return value

def validacao_password(value):
    if len(value) < 8:
        raise ValidationError('A senha deve ter no mínimo 8 caracteres!')
    else:
        return value

def validacao_email(value):
    if '@' not in value:
        raise ValidationError('O email deve ter o "@"')
    else:
        return value

def validacao_data(value):
    try:
        __ = date(value)
    except ValueError:
        raise ValidationError('Data inválida')
