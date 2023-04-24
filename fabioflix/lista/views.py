from django.shortcuts import render, redirect
from conteudo.models import Conteudo
from .models import Lista

# Create your views here.

def salvar(request, id):
    usuario = request.user
    conteudo = Conteudo(id=id)
    
    if request.user in conteudo.salvo.all():
        conteudo.salvo.remove(request.user.id)
        Lista.objects.get(conteudo_id=conteudo).delete()
    else:
        conteudo.salvo.add(request.user.id)
        Lista(usuario=usuario, conteudo=conteudo).save()
    
    return redirect('home')

def assistir_salvo(request, slug):
    conteudo_slug = Conteudo.objects.get(slug=slug)
    conteudo_salvo = Lista.objects.get(slug=conteudo_slug)
        
    context = {
        'conteudo_salvo': conteudo_salvo,
    }
    
    return render(request, 'conteudo.html', context)

