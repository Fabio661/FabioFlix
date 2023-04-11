from django.urls import path

from . import views

urlpatterns = [
    path('add_cesta', views.add_cesta, name='add_cesta'),
]
