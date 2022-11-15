from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Presenca

class PresencaForm(forms.ModelForm):
    data_presenca = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    class Meta:
        model = Presenca
        fields = ['nome_aluno_presenca', 'data_presenca', 'presente']