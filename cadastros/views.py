
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.urls.base import reverse
from .models import Nutriente, Categoria, Sac, Perfil, Alimento, Refeicao
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import GroupRequiredMixin

# Create your views here;


class NutrienteCreate (GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Nutriente
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-nutriente')


class NutrienteUpdate (GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Nutriente
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-nutriente')


class NutrienteDelete (GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Nutriente
    template_name = 'cadastros/formexcluir.html'
    success_url = reverse_lazy('listar-nutriente')


class NutrienteList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = u"Administrador"
    model = Nutriente 
    template_name='cadastros/listar_cadastros.html'

class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    group_required = u"Administrador"
    login_url =  reverse_lazy ('login')
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = ('listar-nutriente')


class CategoriaUpdate (GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('listar-nutriente')


class CategoriaDelete (GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Categoria
    template_name =  'cadastros/formexcluir.html'
    success_url =  reverse_lazy ('listar-nutriente')


class CategoriaList (GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"Administrador"
    login_url = reverse_lazy('login')
    model = Categoria
    template_name='cadastros/listar_cadastros.html'
