from django.shortcuts import render, HttpResponseRedirect
from conteudo.models.conteudo import Conteudo
from salvos.models.salvos import Salvos
from conteudo.forms import LikeForm, ComentarioForm

# Create your views here.

def salvar(request, id):
    id = Conteudo.objects.get(id=id).id
    conteudo = Conteudo.objects.get(id=id)
    usuario = request.user
    esta_salvo = request.user in conteudo.salvo.all()
    url = f'http://127.0.0.1:8000/{id}/'
    
    if esta_salvo:
        conteudo.salvo.remove(usuario)
        Salvos.objects.get(conteudo=conteudo, usuario=usuario).delete()
    else:
        conteudo.salvo.add(usuario)
        Salvos.objects.create(usuario=usuario, conteudo=conteudo)
        
    return HttpResponseRedirect(url)

def assistir_salvo(request, id):
    conteudo_salvo = Salvos.objects.get(usuario=request.user, conteudo_id=id).conteudo_id
    conteudo = Conteudo.objects.get(id=conteudo_salvo)
    comentarios = conteudo.comentarios.filter()
    usuario = request.user
    esta_salvo = request.user in conteudo.salvo.all()
    tem_like = request.user in conteudo.likes.all()
    comentario_form = ComentarioForm(data=request.POST)
    id = Conteudo(id=id).id
   
    #Comentar
    if comentario_form.is_valid():
        novo_comentario = comentario_form.save(commit=False)
        novo_comentario.conteudo = conteudo
        novo_comentario.usuario = usuario
        novo_comentario.save()
        return HttpResponseRedirect(request.path_info)
    else:
        comentario_form = ComentarioForm()   
    
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
        'comentarios': comentarios,
        'esta_salvo': esta_salvo,
        'tem_like':tem_like,
        'comentario_form': comentario_form
    }
    
    return render(request, 'conteudo.html', context)


