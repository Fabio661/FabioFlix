from django.db import models
from conteudo.models.conteudo import Conteudo
from django.contrib.auth.models import User


class Comentario(models.Model):
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_do_comentario')
    comentario = models.TextField(max_length=300)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['criado_em']

    def __str__(self):
        return 'comentario {} por {}'.format(self.conteudo, self.usuario)