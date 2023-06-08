from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/salvar/', views.salvar, name='salvar'),   
    path('<int:id>/salvo/', views.assistir_salvo, name='assistir_salvo'),
]
