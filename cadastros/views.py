
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls.base import reverse
from .models import Nutriente, Categoria, Sac, Perfil, Alimento, Refeicao
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404

# Create your views here;


class RefeicaoCreate (GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Refeicao
    fields = ['horario','quantidade','alimento']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-refeicao')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url


class RefeicaoUpdate (GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Refeicao
    fields = ['horario', 'quantidade', 'alimento']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-refeicao')


    def form_valid(self, form):
     # Define o usuário como usuário logado
     form.instance.usuario = self.request.user
     url = super().form_valid(form)
     #código a fazer depois de salvar objeto no banco
     self.object.atributo = "algo"
     # Salva o objeto novamente
     self.object.save()
     return url

class RefeicaoDelete (GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Refeicao
    fields = ['horario','quantidade','alimento']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-refeicao')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url


class RefeicaoList (GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Refeicao
    template_name = 'cadastros/listar_refeicao.html'

    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView
        self.object_list = Alimento.objects.filter(usuario=self.request.user)
        return self.object_list

class AlimentoCreate (GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Alimento
    fields = ['nome', 'porcao', 'valor_calorico', 'categoria', 'nutriente']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-alimento')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url

class AlimentoUpdate (GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Alimento
    fields = ['nome', 'porcao', 'valor_calorico', 'categoria', 'nutriente']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-alimento')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Alimento, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class AlimentoDelete (GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Alimento
    fields = ['nome', 'porcao', 'valor_calorico', 'categoria', 'nutriente']
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-alimento')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url

class AlimentoList (GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Alimento
    template_name = 'cadastros/listar_alimento.html'

    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView
        self.object_list = Alimento.objects.filter(usuario=self.request.user)
        return self.object_list

class PerfilCreate (GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome', 'sobrenome', 'data_nasc', 'altura', 'peso', 'telefone']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-perfil')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url


class PerfilUpdate (GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome', 'sobrenome', 'data_nasc', 'altura', 'peso', 'telefone']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-perfil')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Perfil, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class PerfilDelete (GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-perfil')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Perfil, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class PerfilList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Perfil
    template_name = 'cadastros/listar_perfil.html'


class NutrienteCreate (GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador",u"Usuários"
    login_url = reverse_lazy('login')
    model = Nutriente
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-nutriente')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url


class NutrienteUpdate (GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Nutriente
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-nutriente')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Nutriente, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class NutrienteDelete (GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Nutriente
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-nutriente')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Nutriente, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class NutrienteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Usuários"
    model = Nutriente
    template_name = 'cadastros/listar_cadastros.html'

    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView
        self.object_list = Nutriente.objects.filter(usuario=self.request.user)
        return self.object_list


class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = ('listar-categoria')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url


class CategoriaUpdate (GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-categoria')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Categoria, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class CategoriaDelete (GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-categoria')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Categoria, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class CategoriaList (GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/listar_categorias.html'

    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView
        self.object_list = Categoria.objects.filter(usuario=self.request.user)
        return self.object_list


class SacCreate (GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Usuário"
    login_url = reverse_lazy('login')
    model = Sac
    fields = ['mensagem']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-sac')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url


class SacUpdate (GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Usuário"
    login_url = reverse_lazy('login')
    model = Sac
    fields = ['mensagem']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-sac')

    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        # código a fazer depois de salvar objeto no banco
        self.object.atributo = "algo"
        # Salva o objeto novamente
        self.object.save()
        return url

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Sac, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class SacDelete (GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Sac
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-sac')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(
            Sac, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class SacList (GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador" u"Usuario"
    login_url = reverse_lazy('login')
    model = Sac
    template_name = 'cadastros/listar_sac.html'

    def get_queryset(self):
        # O object_list armazena uma lista de objetos de um ListView
        self.object_list = Sac.objects.filter(usuario=self.request.user)
        return self.object_list
