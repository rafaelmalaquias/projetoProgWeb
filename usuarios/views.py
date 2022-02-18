from audioop import reverse
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth.models import Group,User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from cadastros.models import Perfil
from .forms import UsuarioForm

# Create your views here.
class UsuarioCreate(CreateView):
    template_name="cadastros/formulario.html"
    model = User
    success_url = reverse_lazy('login')
    form_class = UsuarioForm

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name="Usuários")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url


class UsuarioUpdate(UpdateView):
    template_name = 'cadastros/formulario.html'
    model = Perfil
    fields = ['nome', 'sobrenome','data_nasc', 'altura','peso','telefone']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object
