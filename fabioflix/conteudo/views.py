from django.shortcuts import render
from .models import Conteudo

# Create your views here.

def pagina_inicial(request):
    conteudo = Conteudo.objects.all()
    
    conteudos = {
        'conteudo': conteudo
    }
    
    return render(request, 'home.html', conteudos)