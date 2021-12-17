from django.urls import path

from cadastros.views import CategoriaCreate, CategoriaDelete, CategoriaUpdate, CategoriaList, NutrienteCreate, NutrienteDelete, NutrienteList, NutrienteUpdate


urlpatterns = [
    # Criar todos os endereços/rotas
    #path ('endereço/', MinhaView.as_view(), name='referencia/apelido'),
    path('cadastrar/nutriente/', NutrienteCreate.as_view(), name="cadastrar-nutriente"),
    path('atualizar/nutriente/<int:pk>/',NutrienteUpdate.as_view(), name="atualizar-nutriente"),
    path('excluir/nutriente/<int:pk>/', NutrienteDelete.as_view(), name="deletar-nutriente"),
    path('listar/nutriente/', NutrienteList.as_view(), name="listar-nutriente"),

    path('cadastrar/categoria/', CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path('atualizar/categoria/<int:pk>/',CategoriaUpdate.as_view(), name="atualizar-categoria"),
    path('excluir/categoria/<int:pk>/',CategoriaDelete.as_view(), name="deletar-categoria"),
    path('listar/categoria/', CategoriaList.as_view(), name="listar-categoria")

]
