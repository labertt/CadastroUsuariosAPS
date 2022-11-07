from dataclasses import fields
from enum import unique
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuario.models import Usuario

class NovoUsuarioForm(UserCreationForm):
    username = forms.ChoiceField(choices=[('0', 'Escolha seu user')]+[(Usuario.usernome, Usuario.usernome) for Usuario in Usuario.objects.all()])

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NovoUsuarioForm, self).save(commit=False)
        #user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user