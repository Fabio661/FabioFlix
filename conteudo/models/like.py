from django.db import models
from django.contrib.auth.models import User
from .conteudo import Conteudo

LIKES_ESCOLHAS = (
    ('Like', 'Like'),
    ('Deslike', 'Deslike'),
)

class Like(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.conteudo