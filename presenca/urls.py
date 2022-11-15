from django.urls import path

from presenca.views import PresencaCreateView, ListaPresencaView, PresencaUpdateView, PresencaDeleteView

urlpatterns = [
    path('', ListaPresencaView.as_view(), name='presenca.index'),
    path('novo', PresencaCreateView.as_view(), name='presenca.novo'),
    path('editar/<int:pk>', PresencaUpdateView.as_view(), name='presenca.editar'),
    path('excluir/<int:pk>', PresencaDeleteView.as_view(), name='presenca.excluir'),
]