from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Pagamento

class PagamentoForm(forms.ModelForm):
    data_pagamento = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))
    class Meta:
        model = Pagamento
        fields = ['nome_aluno', 'data_pagamento', 'mes_pagamento', 'forma_pagamento', 'valor_pagamento']