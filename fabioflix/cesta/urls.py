from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/add_cesta', views.add_cesta, name='add_cesta'),
    path('<slug:slug>/', views.assistir_salvo, name='assistir_salvo')
]
