from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, DetailView
from main.models import Jogo, PerguntasJogo, Respostas
from django.contrib import messages
from main.utils.utils_views import get_questions
from datetime import datetime, timedelta
from django.http import HttpResponse, Http404
from django.utils import timezone
from main.utils.generate_slug import generate_slug


def games(request):

    return render(request, 'games.html')

class Game(FormView):
    template_name = 'game.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, 'Você precisa fazer login para jogar.')
            return redirect('login')
        last_game = Jogo.objects.filter(user=request.user).last()
        hora_agora = datetime.now().timestamp()

        if last_game is None:
            get_questions(request)
        else:
            if (last_game.created_at.timestamp() + 600) < hora_agora:   
                # caso a pessoa saia e volte depois
                if last_game.qtd_acertos == 0 or last_game.qtd_erros == 0:
                    messages.info(request, 'Você tem um jogo criado. Continue-o.')
                else:
                    get_questions(request)

            # caso a pessoa termine antes de 10 minutos e queira jogar mais
            elif last_game.qtd_acertos != 0 or last_game.qtd_erros != 0:
                get_questions(request)
            else:
                messages.error(request, 'Você tem um jogo criado a menos de 10 minutos. Continue este.')
        
        game_selected = Jogo.objects.filter(user=request.user).last()
        return render(request, self.template_name, context={'perguntas': PerguntasJogo.objects.filter(game=game_selected)})
    
    def post(self, request, *args, **kwargs):
        respostas = {}

        for key, value in request.POST.items():
            if key.startswith("resposta_") or key.startswith("jogo"):
                respostas[key] = value

        game = Jogo.objects.filter(pk=respostas['jogo']).last()

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
        return redirect('main:game_resume', slug=game.slug)

class GameResume(DetailView):
    model = Jogo
    template_name = 'game_detail.html'

    def get_object(self):
        return get_object_or_404(Jogo, slug=self.kwargs.get('slug'))
        

    def get(self, request, *args, **kwargs): 
        game = self.get_object()
        try:
            game_duration = game.finished_at - game.created_at
        except TypeError:
            raise Http404('Jogo provavelmente não finalizado')

        total_questions = game.qtd_acertos + game.qtd_erros
        context = {
            'game_model': game,
            'game_duration': game_duration,
            'total_questions': total_questions,
        }
        
        return render(request, self.template_name, context)