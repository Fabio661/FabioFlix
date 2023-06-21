from django.test import TestCase
from conteudo.factories import ConteudoFactory, UsuarioFactory
from salvos.models.salvos import Salvos

class SalvarTest(TestCase):
    
    def setUp(self):
        
        self.usuario = UsuarioFactory(
            username = 'testusuario'
        )
        
        self.client.force_login(user=self.usuario) 
               
        self.conteudo = ConteudoFactory(
            id = 1,
            titulo='titulo',
            slug='teste-titulo',
            imagem='imagems/the-end-of-the-fucking-world_wMpI6Y3.jpg',
            sinopse='teste sinopse',
            idade_recomendada=18,
            status='Normal',
            genero='Filme',
            genero_cinematografico='Acao'
        )
        
    def test_salvar_conteudo(self):
        
        if self.conteudo.id not in Salvos.objects.all():
            Salvos.objects.create(usuario=self.usuario, conteudo=self.conteudo)
        else:
            raise Exception('Conteudo ja está salvo')
              
        conteudo_salvo = Salvos.objects.get(conteudo_id=1).conteudo_id
        self.assertEqual(conteudo_salvo, self.conteudo.id)
        
   