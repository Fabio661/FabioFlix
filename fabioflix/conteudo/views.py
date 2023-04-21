from django.shortcuts import render, redirect
from .models import Conteudo
from cesta.models import Cesta

# Create your views here.

def pagina_inicial(request):
    conteudo = Conteudo.objects.all()
    salvos = Cesta.objects.filter(usuario = request.user)
    
    conteudos = {
        'conteudo': conteudo,     
        'salvos': salvos 
    }
    
    return render(request, 'home.html', conteudos)

def darlike(request, id):
    conteudo = Conteudo(id=id)
    conteudo.likes.add(request.user.id)
    return redirect('home'+str(conteudo))

def assistir(request, slug):
    conteudo = Conteudo.objects.get(slug=slug)
    
    context = {
        'conteudo': conteudo
    }
    
    return render(request, 'conteudo.html', context)