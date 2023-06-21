from django import forms
from .models.like import Like
from .models.comentario import Comentario

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ('usuario', 'conteudo',)
        
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('comentario',)