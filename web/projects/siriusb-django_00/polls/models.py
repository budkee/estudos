import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Pergunta(models.Model):
    textoDaPergunta = models.CharField(max_length=200)

    dataDePublicacao = models.DateTimeField('data de publicação')
    
    def __str__(self):
        return self.textoDaPergunta
    def foiPublicadoRecentemente(self):
        return self.dataDePublicacao >= timezone.now() - datetime.timedelta(days=1)


class Escolha(models.Model):
    
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE) # Relação: cada choice está relacionada a uma única question [Relacionamentos mais comuns](https://docs.djangoproject.com/pt-br/4.0/intro/tutorial02/)

    criadoEm = models.DateTimeField(default=timezone.now)

    campoDaEscolha = models.CharField('texto de escolha',max_length=200)
    
    votos = models.IntegerField('votos', default=0)

    def __def__(self):
        return self.campoDaEscolha