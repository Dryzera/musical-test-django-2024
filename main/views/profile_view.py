from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from main.models import UserPerfil, Jogo
from django.contrib import messages

class ProfileHome(DetailView):
    model = UserPerfil
    template_name = 'profile.html'

    def get(self, *args, **kwargs):
        self.id = self.kwargs['pk']
        # fix bug - not found user
        self.usuario = get_object_or_404(UserPerfil, user=self.id)

        return super().get(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = self.usuario
        context['pk'] = self.kwargs['pk']

        return context
    
def profile_resume_games(request, pk):
    context = {}

    game = Jogo.objects.filter(user=pk).all().order_by('-pk')
    usuario = UserPerfil.objects.get(user=pk)

    context['games'] = game
    context['user'] = usuario
    context['pk'] = pk

    return render(request, 'profile_resume_games.html', context)