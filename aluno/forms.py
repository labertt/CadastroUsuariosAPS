from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    data_nascimento_aluno = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    class Meta:
        model = Aluno
        fields = ['nome_completo_aluno', 'cpf_aluno', 'data_nascimento_aluno', 'endereco_aluno', 'turno_aluno', 'arte_marcial_aluno']