from django.urls import path
from .views import PaginaInicial, Sobre,Inicio

urlpatterns = [
    # Criar todos os endereços/rotas
    #path ('endereço/', MinhaView.as_view(), name='referencia/apelido'),
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', Sobre.as_view(), name='sobre'),
    path('inicio/',Inicio.as_view(), name='inicio'),
]
