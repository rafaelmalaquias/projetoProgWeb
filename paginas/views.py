from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView



class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'


class Sobre(TemplateView):
    template_name = 'paginas/sobre.html'
# Create your views here.
