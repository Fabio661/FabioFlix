import factory

from django.contrib.auth.models import User
from conteudo.models.conteudo import Conteudo

class UsuarioFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('pystr')
    
    class Meta:
        model = User

class ConteudoFactory(factory.django.DjangoModelFactory):
    titulo = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    
    class Meta:
        model = Conteudo