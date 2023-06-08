from django.shortcuts import render,redirect, HttpResponse, HttpResponseRedirect
from conteudo.models.conteudo import Conteudo
from .models import Lista
from conteudo.forms import LikeForm
# Create your views here.

def salvar(request, id):
    id = Conteudo.objects.get(id=id).id
    conteudo = Conteudo.objects.get(id=id)
    usuario = request.user
    tem_like = usuario in conteudo.likes.all()
    esta_salvo = request.user in conteudo.salvo.all()
    url = f'http://127.0.0.1:8000/{id}/'
    
    if request.method == 'POST':
        like_form = LikeForm(data=request.POST)
        if like_form.is_valid() and tem_like:
            conteudo.likes.remove(request.user)
            return HttpResponseRedirect(request.path_info)
        else:
            conteudo.likes.add(request.user.id)
            return HttpResponseRedirect(request.path_info)
    else:
        like_form = LikeForm()
    
    if esta_salvo:
        conteudo.salvo.remove(usuario)
        Lista.objects.get(conteudo=conteudo, usuario=usuario).delete()
    else:
        conteudo.salvo.add(usuario)
        Lista.objects.create(usuario=usuario, conteudo=conteudo)
        
    return HttpResponseRedirect(url)

def assistir_salvo(request, id):
    usuario = request.user
    conteudo_salvo = Lista.objects.get(usuario=usuario, conteudo_id=id).conteudo_id
    conteudo = Conteudo.objects.get(id=conteudo_salvo)
    esta_salvo = request.user in conteudo.salvo.all()
    tem_like = request.user in conteudo.likes.all()
    id = Conteudo(id=id).id
    
    if request.method == 'POST':
        like_form = LikeForm(data=request.POST)
        if like_form.is_valid() and tem_like:
            conteudo.likes.remove(request.user)
            return HttpResponseRedirect(request.path_info)
        else:
            conteudo.likes.add(request.user.id)
            return HttpResponseRedirect(request.path_info)
    else:
        like_form = LikeForm()
    
    context = {
        'conteudo': conteudo,
        'esta_salvo': esta_salvo,
        'tem_like':tem_like,
    }
    
    return render(request, 'conteudo.html', context)


