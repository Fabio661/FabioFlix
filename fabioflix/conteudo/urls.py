from django.urls import path

from conteudo import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('like/<int:id>', views.darlike, name='darlike'),
    path('<slug:slug>/', views.assistir, name='assistir')
]
