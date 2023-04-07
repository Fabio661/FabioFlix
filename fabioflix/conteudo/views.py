from django.shortcuts import render, redirect
from .models import Conteudo
from django.shortcuts import get_list_or_404

# Create your views here.

def pagina_inicial(request):
    conteudo = Conteudo.objects.all()
    
    conteudos = {
        'conteudo': conteudo
    }
    
    return render(request, 'home.html', conteudos)