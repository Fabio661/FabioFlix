from django.contrib import admin
from conteudo.models import Conteudo


# Register your models here.

class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'status', 'criado_em')
    list_filter = ('genero',)
    search_fields = ('titulo', 'sinopse')
    readonly_fields = ('id',)
    prepopulated_fields = {'slug' : ('titulo',)}

admin.site.register(Conteudo, ConteudoAdmin)