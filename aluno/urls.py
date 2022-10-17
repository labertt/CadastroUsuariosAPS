from django.urls import path

from aluno.views import AlunoCreateView, ListaAlunoView, AlunoUpdateView, AlunoDeleteView

urlpatterns = [
    path('', ListaAlunoView.as_view(), name='aluno.index'),
    path('novo', AlunoCreateView.as_view(), name='aluno.novo'),
    path('editar/<int:pk>', AlunoUpdateView.as_view(), name='aluno.editar'),
    path('excluir/<int:pk>', AlunoDeleteView.as_view(), name='aluno.excluir'),
]