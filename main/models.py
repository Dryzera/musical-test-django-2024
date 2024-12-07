from django.db import models
from django.contrib.auth.models import User

class Localidade(models.Model):
    localidade = models.CharField(max_length=500, blank=False, null=False)

class UserPerfil(models.Model):
    CARGO_CHOICES = [
        ('Candidato', 'candidato'),
        ('Instrutor', 'instrutor'),
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    localidade = models.ForeignKey(Localidade, on_delete=models.SET_NULL, null=True)
    cargo = models.CharField(choices=CARGO_CHOICES, max_length=15, blank=False)

    class Meta:
        verbose_name = 'Perfil de úsuario'

class Perguntas(models.Model):
    FASES_MSA_CHOICES = [
        ('1', 'Fase 1'),
        ('2', 'Fase 2'),
        ('3', 'Fase 3'),
        ('4', 'Fase 4'),
        ('5', 'Fase 5'),
        ('6', 'Fase 6'),
        ('7', 'Fase 7'),
        ('8', 'Fase 8'),
        ('9', 'Fase 9'),
        ('10', 'Fase 10'),
        ('11', 'Fase 11'),
        ('12', 'Fase 12'),
        ('13', 'Fase 13'),
        ('14', 'Fase 14'),
        ('15', 'Fase 15'),
        ('16', 'Fase 16')
    ]
    NIVEL_DIFICULDADE_CHOICE = [
        ('Muito Facil', 'Muito Facil'),
        ('Facil', 'Facil'),
        ('Intermediário', 'Intermediário'),
        ('Difícil', 'Difícil'),
        ('Muito Difícil', 'Muito Difícil'),
    ]


    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False)
    pergunta = models.CharField(max_length=200)
    fase = models.CharField(choices=FASES_MSA_CHOICES, max_length=10, blank=False)
    dificuldade = models.CharField(choices=NIVEL_DIFICULDADE_CHOICE, max_length=13, blank=False)


    class Meta:
        verbose_name_plural = 'Perguntas'

    def __str__(self):
        return self.pergunta

class Respostas(models.Model):
    pergunta = models.ForeignKey(Perguntas, on_delete=models.CASCADE, related_name="respostas")
    resposta = models.CharField(max_length=200, blank=False)
    resposta_correta = models.BooleanField(default=False)

class Jogo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    qtd_erros = models.PositiveIntegerField(default=0)
    qtd_acertos = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Jogo de {self.user}'

class PerguntasJogo(models.Model):
    game = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name="perguntas_jogo")
    question = models.ForeignKey(Perguntas, on_delete=models.SET_NULL, null=True, related_name="jogos")

    def __str__(self):
        return f'Perguntas do jogo {self.game}'
