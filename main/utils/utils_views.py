from django.http import HttpResponse
from main.models import Jogo, Perguntas, PerguntasJogo
from random import sample

def get_questions(request):
    game = Jogo.objects.create(user=request.user)
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