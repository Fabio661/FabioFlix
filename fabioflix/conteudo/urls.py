from django.urls import path

from conteudo import views

urlpatterns = [
    path('', views.pagina_inicial, name='home')
]
