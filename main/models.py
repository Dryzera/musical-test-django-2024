from django.db import models
from django.contrib.auth.models import User

class Localidade(models.Model):
    localidade = models.CharField(max_length=500, blank=False, null=False)

class UserPerfil(models.Model):
    CARGO_CHOICES = [
        ('Candidato', 'candidato'),
        ('Instrutor', 'instrutor'),
    ]
    localidade = models.ForeignKey(Localidade, on_delete=models.SET_NULL, null=True)
    cargo = models.CharField(choices=CARGO_CHOICES, max_length=15, blank=False)

class Perguntas(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pergunta = models.CharField(max_length=200)

class Respostas(models.Model):
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE, related_name="respostas")
    resposta = models.CharField(max_length=200, blank=False)
    resposta_correta = models.BooleanField(default=False)

class Jogo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    qtd_erros = models.PositiveIntegerField(default=0)
    qtd_acertos = models.PositiveIntegerField(default=0)

class PerguntasJogo(models.Model):
    game = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name="perguntas_jogo")
    question = models.ForeignKey(Perguntas, on_delete=models.SET_NULL, null=True, related_name="jogos")
