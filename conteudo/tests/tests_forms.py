from django.test import TestCase
from conteudo.factories import ConteudoFactory, UsuarioFactory
from conteudo.forms import LikeForm

class DarLikeTest(TestCase):
    
    def setUp(self):
        
        self.usuario = UsuarioFactory(username = 'testusuario')
        
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

    def test_dar_like(self):
          
        data = {
            'usuario': self.usuario,
            'conteudo': self.conteudo,
            'likes': 0
        }
        
        form = LikeForm(data=data)
        
        if form.is_valid():
            data['likes'] += 1
            
        self.assertTrue(form.is_valid())
        self.assertEqual(data['likes'], 1)
        