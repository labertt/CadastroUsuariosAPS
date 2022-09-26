from django.urls import path
from .views import ListaUsuarioView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListaUsuarioView.as_view()), name='usuario.index'),
    path('novo/', login_required(UsuarioCreateView.as_view()), name='usuario.novo'),
    path('editar/<int:pk>', login_required(UsuarioUpdateView.as_view()), name='usuario.editar'),
    path('excluir/<int:pk>', login_required(UsuarioDeleteView.as_view()), name='usuario.excluir')
]