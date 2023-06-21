from django.contrib import admin
from salvos.models.salvos import Salvos

# Register your models here.

class ListaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'conteudo')
    list_filter = ('conteudo', 'usuario')

admin.site.register(Salvos, ListaAdmin)