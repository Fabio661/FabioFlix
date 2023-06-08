from django.urls import path
from conteudo import views

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('<int:id>/', views.assistir, name='assistir'),
]
