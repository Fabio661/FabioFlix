from django.db import models
from conteudo.models import Conteudo
from django.contrib.auth.models import User

# Create your models here.

class Lista(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE, related_name='conteudo_lista')
    