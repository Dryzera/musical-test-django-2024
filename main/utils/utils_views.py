from django.http import HttpResponse
from main.models import Jogo, Perguntas, PerguntasJogo
from random import sample
from datetime import datetime
from django.utils import timezone
from main.utils.generate_slug import generate_slug

def get_questions(request):
    game = Jogo.objects.create(user=request.user)
    if not game.slug:
        game.slug = generate_slug()
        game.save()
    perguntas = list(Perguntas.objects.all())
    qtd_perguntas = len(perguntas)

    if qtd_perguntas == 0:
        return HttpResponse("Nenhuma pergunta disponível.", status=404)
    num_perguntas_desejadas = 10

    if num_perguntas_desejadas > qtd_perguntas:
        num_perguntas_desejadas = qtd_perguntas
    perguntas_selecionadas = sample(perguntas, num_perguntas_desejadas)

    for pergunta in perguntas_selecionadas:
        PerguntasJogo.objects.create(game=game, question=pergunta)
    return HttpResponse("Jogo iniciado com sucesso.")