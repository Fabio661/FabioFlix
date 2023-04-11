from django.shortcuts import render, redirect
from conteudo.models import Conteudo
from .models import Cesta

# Create your views here.

def add_cesta(request):
    usuario = request.user
    conteudo_id = Conteudo.objects.get().id
    conteudo = Conteudo.objects.get(id=conteudo_id)
    Cesta(usuario=usuario, conteudo=conteudo).save()
    
    return redirect('home')