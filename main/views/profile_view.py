from django.shortcuts import render, redirect
from django.views.generic import DetailView
from main.models import UserPerfil, Jogo
from django.contrib import messages

class ProfileHome(DetailView):
    model = UserPerfil
    template_name = 'profile.html'

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'Você não está logado. Faça login abaixo.')
            return redirect('main:home')

        self.id = self.kwargs['pk']
        self.usuario = UserPerfil.objects.get(user=self.id)

        return super().get(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = self.usuario

        return context
    
def profile_resume_games(request, pk):
    context = {}

    game = Jogo.objects.filter(user=pk).all()
    usuario = UserPerfil.objects.get(user=pk)

    context['games'] = game
    context['user'] = usuario

    return render(request, 'profile_resume_games.html', context)