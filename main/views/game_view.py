from django.shortcuts import render, redirect
from django.views.generic import FormView
from main.models import Jogo, Perguntas, PerguntasJogo
from random import choice, sample
from django.http import HttpResponse
from django.contrib import messages


def games(request):
    return render(request, 'games.html')

class Game(FormView):
    template_name = 'game.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Você precisa fazer login para jogar.')
            return redirect('login')
        
        def get_questions():
            game = Jogo.objects.create(user=request.user)
            perguntas = list(Perguntas.objects.all())
            qtd_perguntas = len(perguntas)

            if qtd_perguntas == 0:
                return HttpResponse("Nenhuma pergunta disponível.", status=404)
            num_perguntas_desejadas = 0

            if num_perguntas_desejadas > qtd_perguntas:
                num_perguntas_desejadas = qtd_perguntas
            perguntas_selecionadas = sample(perguntas, num_perguntas_desejadas)

            for pergunta in perguntas_selecionadas:
                PerguntasJogo.objects.create(game=game, question=pergunta)
            return HttpResponse("Jogo iniciado com sucesso.")

        get_questions()
        user_games = Jogo.objects.filter(user=request.user).first()
        return render(request, self.template_name, context={'perguntas': PerguntasJogo.objects.filter(game=user_games)})
