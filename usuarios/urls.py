from django import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import UsuarioCreate, UsuarioUpdate

urlpatterns = [
    # Aqui vão suas urls
    path('login/', auth_views.LoginView.as_view(
        template_name='usuarios/login.html',
        extra_context={'titulo': 'Autenticação'}
    ), name='login'),

    path('sair/', auth_views.LogoutView.as_view(), name="logout"),

    path('alterarsenha/', auth_views.PasswordChangeView.as_view(
        template_name='usuarios/trocar_senha.html',
        extra_context={'titulo': 'Alterar senha atual'},
        success_url=reverse_lazy('index')
    ), name="alterar-senha"),

    path('registrar/', UsuarioCreate.as_view(), name='registrar'),

    path('atualizar/',UsuarioUpdate.as_view(),name='atualizar')

]
