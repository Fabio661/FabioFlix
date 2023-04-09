from django.shortcuts import render, redirect
from .models import Conteudo

# Create your views here.

def pagina_inicial(request):
    conteudo = Conteudo.objects.all()
    
    conteudos = {
        'conteudo': conteudo      
    }
    
    return render(request, 'home.html', conteudos)

def darlike(request, pk):
    conteudo = Conteudo(id=pk)
    conteudo.likes.add(request.user.id)
    return redirect('home'+str(conteudo))

def assistir(request, id):
    conteudo = Conteudo.objects.get(id=id)
    
    conteudos = {
        'conteudo': conteudo
    }
    
    return render(request, 'conteudo.html', conteudos)