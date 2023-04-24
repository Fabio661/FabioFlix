from django.shortcuts import render, redirect
from .models import Conteudo
from lista.models import Lista

# Create your views here.

def pagina_inicial(request):
    conteudo = Conteudo.objects.all()
    salvos = Lista.objects.filter(usuario=request.user.id)
     
    context = {
        'conteudo': conteudo,     
        'conteudo_salvo': salvos,
    }
    
    return render(request, 'home.html', context)

def darlike(request, id):
    conteudo = Conteudo(id=id)
      
    if request.user in conteudo.likes.all():
        conteudo.likes.remove(request.user)
    else:
        conteudo.likes.add(request.user.id)  
        
    return redirect('home'+str(conteudo))

def assistir(request, slug):
    conteudo = Conteudo.objects.get(slug=slug)
    tem_like = request.user in conteudo.likes.all()
    esta_salvo = request.user in conteudo.salvo.all()
    
    context = {
        'conteudo': conteudo,
        'tem_like': tem_like,
        'esta_salvo': esta_salvo
    }
    
    return render(request, 'conteudo.html', context)
