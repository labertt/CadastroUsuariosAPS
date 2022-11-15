from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Presenca
from .forms import PresencaForm

class ListaPresencaView(ListView):
    model = Presenca
    queryset = Presenca.objects.all().order_by('nome_aluno_presenca')

    def get_queryset(self):
        queryset = super().get_queryset()

        filto_nome = self.request.GET.get('nome') or None
        if filto_nome:
            queryset = queryset.filter(nome_aluno_presenca__contains=filto_nome)
        return queryset

class PresencaCreateView(CreateView):
    model = Presenca
    form_class = PresencaForm
    success_url = '/presencas'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PresencaUpdateView(UpdateView):
    model = Presenca
    form_class = PresencaForm
    success_url = '/presencas'

class PresencaDeleteView(DeleteView):
    model = Presenca
    success_url = '/presencas'