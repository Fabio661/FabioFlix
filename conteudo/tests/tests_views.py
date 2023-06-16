from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from conteudo.factories import ConteudoFactory, UsuarioFactory


class AssistirTeste(TestCase):
    
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
        
    def test_lista_conteudo_usuario_autenticado_e_nao_auntenticado(self):
        url = reverse('home')
        response = self.client.get(url)
        
        if self.client.logout():
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_visualizar_conteudo_usuario_logado_e_nao_logado(self):          
        url = reverse('assistir', args=[self.conteudo.id])
        response = self.client.get(url)
        
        if self.client.logout():
            self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        else:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
