from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Aluno
from .forms import AlunoForm

class ListaAlunoView(ListView):
    model = Aluno
    queryset = Aluno.objects.all().order_by('nome_completo_aluno')

    def get_queryset(self):
        queryset = super().get_queryset()

        filto_nome = self.request.GET.get('nome') or None
        if filto_nome:
            queryset = queryset.filter(nome_completo_aluno__contains=filto_nome)
        return queryset

class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    success_url = '/alunos'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    success_url = '/alunos'

class AlunoDeleteView(DeleteView):
    model = Aluno
    success_url = '/alunos'