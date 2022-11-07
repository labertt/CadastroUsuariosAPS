from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    class Meta:
        model = Usuario
        fields = ['nome_completo', 'cpf', 'data_nascimento', 'endereco', 'email', 'usernome']