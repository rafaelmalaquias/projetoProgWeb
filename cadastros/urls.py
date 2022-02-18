from django.urls import path

from cadastros.views import AlimentoCreate, AlimentoDelete, AlimentoList, AlimentoUpdate, CategoriaCreate, CategoriaDelete, CategoriaUpdate, CategoriaList, NutrienteCreate, NutrienteDelete, NutrienteList, NutrienteUpdate, PerfilCreate, PerfilDelete, PerfilList, PerfilUpdate, RefeicaoCreate, RefeicaoDelete, RefeicaoList, RefeicaoUpdate, SacCreate,SacUpdate,SacDelete,SacList
PerfilCreate,PerfilUpdate,PerfilDelete,PerfilList,AlimentoCreate,AlimentoDelete,AlimentoUpdate,AlimentoList,RefeicaoCreate,RefeicaoDelete,RefeicaoUpdate,RefeicaoList

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
    path('listar/categoria/', CategoriaList.as_view(), name="listar-categoria"),

    path('cadastrar/sac/', SacCreate.as_view(),name="cadastrar-sac"),
    path('atualizar/sac/<int:pk>/', SacUpdate.as_view(), name="atualizar-sac"),
    path('excluir/sac/<int:pk>/',SacDelete.as_view(), name="deletar-sac"),
    path('listar/sac/', SacList.as_view(), name="listar-sac"),

    path('cadastrar/perfil/', PerfilCreate.as_view(), name="cadastrar-perfil"),
    path('atualizar/perfil/<int:pk>/', PerfilUpdate.as_view(), name="atualizar-perfil"),
    path('excluir/perfil/<int:pk>/', PerfilDelete.as_view(), name="deletar-perfil"),
    path('listar/perfil/', PerfilList.as_view(), name="listar-perfil"),

    path('cadastrar/alimento/', AlimentoCreate.as_view(), name="cadastrar-alimento"),
    path('atualizar/alimento/<int:pk>/',AlimentoUpdate.as_view(), name="atualizar-alimento"),
    path('excluir/alimento/<int:pk>/', AlimentoDelete.as_view(), name="deletar-alimento"),
    path('listar/alimento/', AlimentoList.as_view(), name="listar-alimento"),

    path('cadastrar/refeicao/', RefeicaoCreate.as_view(),
         name="cadastrar-refeicao"),
    path('atualizar/refeicao/<int:pk>/',
         RefeicaoUpdate.as_view(), name="atualizar-refeicao"),
    path('excluir/refeicao/<int:pk>/',
         RefeicaoDelete.as_view(), name="deletar-refeicao"),
    path('listar/refeicao/', RefeicaoList.as_view(), name="listar-refeicao"),
]
