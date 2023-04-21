from django.shortcuts import render, redirect
from conteudo.models import Conteudo
from .models import Cesta

# Create your views here.

def add_cesta(request, id):
    usuario = request.user
    conteudo_id = Conteudo.objects.get(id=id).id
    conteudo = Conteudo.objects.get(id=conteudo_id)
    Cesta(usuario=usuario, conteudo=conteudo).save()
    
    return redirect('home')

def assistir_salvo(request, slug):
    
    salvo_slug = conteudo = Conteudo.objects.get(slug=slug)
    conteudo_salvo = Cesta.objects.get(request.user.id, slug=salvo_slug)
    
    context = {
        'salvos': conteudo_salvo
    }
    
    return render(request, 'conteudo.html', context)