from django.db import models
from polymorphic import PolymorphicModel

# Create your models here.
class Pessoa(PolymorphicModel):
	nome = models.CharField(max_length=100)

class Fisica(Pessoa):
	sobrenome = models.CharField(max_length=100)

class Juridica(Pessoa):
	razao_social = models.CharField(max_length=200)

class Participante(models.Model):
	pessoa = models.ForeignKey(Pessoa)
	status = models.CharField(max_length=30)