from django.shortcuts import render, redirect
from django.views.generic import FormView
from main.models import Jogo, Perguntas, PerguntasJogo, Respostas
from random import choice, sample
from django.http import HttpResponse
from django.contrib import messages
from main.utils.utils_views import get_questions
from datetime import datetime


def games(request):
    return render(request, 'games.html')

class Game(FormView):
    template_name = 'game.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Você precisa fazer login para jogar.')
            return redirect('login')

        user_games = Jogo.objects.filter(user=request.user).last()
        hora_agora = datetime.now().timestamp()

        if user_games is None:
            get_questions(request)
        else:
            if (user_games.created_at.timestamp() + 600) < hora_agora:   
                # caso a pessoa saia e volte depois
                if user_games.qtd_acertos == 0 or user_games.qtd_erros == 0:
                    messages.info(request, 'Você tem um jogo criado. Continue-o.')
                else:
                    get_questions(request)

            # caso a pessoa termine antes de 10 minutos e queira jogar mais
            elif user_games.qtd_acertos != 0 or user_games.qtd_erros != 0:
                get_questions(request)
            else:
                messages.error(request, 'Você tem um jogo criado a menos de 10 minutos. Continue este.')

        return render(request, self.template_name, context={'perguntas': PerguntasJogo.objects.filter(game=user_games)})
    
    def post(self, request, *args, **kwargs):
        respostas = {}

        for key, value in request.POST.items():
            if key.startswith("resposta_") or key.startswith("jogo"):
                respostas[key] = value
        
        print(respostas)

        game = Jogo.objects.filter(pk=respostas['jogo']).first()

        for resposta in respostas.values():
            if resposta == respostas['jogo']:
                continue
            resposta_correta = Respostas.objects.filter(pk=resposta).first()
            if resposta_correta.resposta_correta:
                game.qtd_acertos += 1
                game.save()
            else:
                game.qtd_erros += 1
                game.save()
        game.finished_at = datetime.now()
        game.save()
        return redirect('main:game_resume')
