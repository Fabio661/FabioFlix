from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastrarConta(TestCase):
    
    def test_cadastrar_conta(self):
        
        data = {
            'username': 'testusuario',
            'password1': 'Senhateste',
            'password2': 'Senhateste',
        }
        
        form = UserCreationForm(data=data)
        
        if form.is_valid():
            User.objects.create_user(username=data['username'])
        else:
            pass
        
        novo_usuario = User.objects.get(username=data['username'])
        
        self.assertEqual(novo_usuario.username, data['username'])
        self.assertTrue(form.is_valid())