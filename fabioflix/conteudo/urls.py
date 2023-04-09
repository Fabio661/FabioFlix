from django.urls import path

from conteudo import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('like/<int:pk>', views.darlike, name='darlike'),
    path('<int:id>', views.assistir, name='assistir')
]
