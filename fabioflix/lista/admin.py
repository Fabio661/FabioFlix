from django.contrib import admin
from .models import Lista

# Register your models here.

class ListaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'conteudo')
    list_filter = ('conteudo', 'usuario')

admin.site.register(Lista, ListaAdmin)