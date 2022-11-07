from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pagamento
from .forms import PagamentoForm

class ListaPagamentoView(ListView):
    model = Pagamento
    queryset = Pagamento.objects.all().order_by('nome_aluno')

    def get_queryset(self):
        queryset = super().get_queryset()

        filto_nome = self.request.GET.get('nome') or None
        if filto_nome:
            queryset = queryset.filter(nome_aluno__contains=filto_nome)
        return queryset

class PagamentoCreateView(CreateView):
    model = Pagamento
    form_class = PagamentoForm
    success_url = '/pagamentos'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PagamentoUpdateView(UpdateView):
    model = Pagamento
    form_class = PagamentoForm
    success_url = '/pagamentos'

class PagamentoDeleteView(DeleteView):
    model = Pagamento
    success_url = '/pagamentos'