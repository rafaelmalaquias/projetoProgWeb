from django.db import models
from django.db.models.fields import DecimalField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Nutriente(models.Model):
    nome = models.CharField(max_length=255)

    def __str__ (self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__ (self):
        return self.nome

class Sac(models.Model):
    categoria = models.CharField(max_length=255)
   
    def __str__(self):
        return self.categoria

class Perfil(models.Model):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=255)
    data_nasc= models.DateField()
    altura = models.DecimalField(max_digits = 4, decimal_places=2)
    peso = models.DecimalField(max_digits = 5, decimal_places=2)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome + ' ' + str(self.sobrenome) + ' - ' + str(self.data_nasc) + ' - ' + str(self.peso)

class Alimento(models.Model):
    nome = models.CharField(max_length=255)
    porcao = models.DecimalField(max_digits=5,decimal_places=2)
    valor_calorico=models.FloatField()
    categoria = ForeignKey(Categoria, on_delete=models.PROTECT)
    nutriente = ForeignKey(Nutriente,on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' - ' + str(self.valor_calorico) +'/'+str(self.porcao)

class Refeicao(models.Model):
    horario = models.DateTimeField()
    quantidade = models.DecimalField(max_digits = 6, decimal_places=2)
    alimento = ForeignKey(Alimento, on_delete=models.PROTECT)

    def __str__(self):
        return self.horario + ' - ' + str(self.alimento) + ' - ' + str(self.quantidade)
