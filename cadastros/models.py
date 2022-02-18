from django.db import models
from django.db.models.fields import DecimalField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Nutriente(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=255)

    def __str__ (self):
        return self.nome

class Categoria(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=255)
    
    def __str__ (self):
        return self.nome

class Sac(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    mensagem = models.CharField(max_length=255)
   
    def __str__(self):
        return self.mensagem

class Perfil(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=25,null=True)
    sobrenome = models.CharField(max_length=255, null=True)
    data_nasc = models.DateField(null=True)
    altura = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    telefone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.nome + ' ' + str(self.sobrenome) + ' - ' + str(self.data_nasc) + ' - ' + str(self.peso)

class Alimento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(max_length=255)
    porcao = models.DecimalField(max_digits=5,decimal_places=2)
    valor_calorico=models.FloatField()
    categoria = ForeignKey(Categoria, on_delete=models.PROTECT)
    nutriente = ForeignKey(Nutriente,on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' - ' + str(self.valor_calorico) +'/'+str(self.porcao)

class Refeicao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    horario = models.DateTimeField()
    quantidade = models.DecimalField(max_digits = 6, decimal_places=2)
    alimento = ForeignKey(Alimento, on_delete=models.PROTECT)

    def __str__(self):
        return self.horario + ' - ' + str(self.alimento) + ' - ' + str(self.quantidade)
