from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Usuario
from .forms import UsuarioForm

class ListaUsuarioView(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user)

        filto_nome = self.request.GET.get('nome') or None
        if filto_nome:
            queryset = queryset.filter(nome_completo__contains=filto_nome)
        return queryset

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = '/usuarios'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    success_url = '/usuarios'

class UsuarioDeleteView(DeleteView):
    model = Usuario
    success_url = '/usuarios'