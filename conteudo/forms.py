from django import forms
from .models.like import Like

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ('usuario', 'conteudo',)