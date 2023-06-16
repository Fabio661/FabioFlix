from django.shortcuts import render,redirect, HttpResponseRedirect
from django.views.generic import ListView
from .models.conteudo import Conteudo
from lista.models.lista import Lista
from .forms import LikeForm

# Create your views here.

def pagina_inicial(request):
    conteudo = Conteudo.objects.all()
    salvos = Lista.objects.filter(usuario=request.user.id)
     
    context = {
        'conteudo': conteudo,     
        'conteudo_salvo': salvos,
    }
    
    return render(request, 'home.html', context)

def assistir(request, id):
    if request.user.is_authenticated:
        conteudo = Conteudo.objects.get(id=id)
        tem_like = request.user in conteudo.likes.all()
        esta_salvo = request.user in conteudo.salvo.all()
        
        #Like
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
            'tem_like': tem_like,
            'esta_salvo': esta_salvo,
            'like_form': like_form,
        }
        
        return render(request, 'conteudo.html', context)
    
    else:       
        return redirect('cadastro')

class EncontrarConteudo(ListView):
    model = Conteudo
    conteudos = Conteudo.objects.all()
    template_name = 'procurar.html'
    
    def get_queryset(self):
        txt_titulo = self.request.GET.get('titulo')
           
        if txt_titulo:    
            conteudos = Conteudo.objects.filter(titulo__icontains=txt_titulo)
        else:
            conteudos = Conteudo.objects.all()
            
        return conteudos