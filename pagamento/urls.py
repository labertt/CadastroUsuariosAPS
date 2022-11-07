from django.urls import path

from pagamento.views import PagamentoCreateView, ListaPagamentoView, PagamentoUpdateView, PagamentoDeleteView

urlpatterns = [
    path('', ListaPagamentoView.as_view(), name='pagamento.index'),
    path('novo', PagamentoCreateView.as_view(), name='pagamento.novo'),
    path('editar/<int:pk>', PagamentoUpdateView.as_view(), name='pagamento.editar'),
    path('excluir/<int:pk>', PagamentoDeleteView.as_view(), name='pagamento.excluir'),
]