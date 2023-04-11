from django.db import models
from conteudo.models import Conteudo
from django.contrib.auth.models import User

# Create your models here.

class Cesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)