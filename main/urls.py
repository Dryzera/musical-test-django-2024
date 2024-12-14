from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'main'

urlpatterns = [
    # perfil urls
    path('perfil/<int:pk>/resumegames/', view=index, name='resumegames'),
    path('perfil/<int:pk>/', view=ProfileHome.as_view(), name='perfil'),

    # game urls
    path('game/<int:pk>/', view=Game.as_view(), name='game'),
    path('game/resume/', view=index, name='game_resume'),
    path('games/', view=games, name='games'),

    # generic urls
    path('search/<slug:slug>/', view=index, name='search'),
    path('logout/', view=logout_user, name='logout'),
    path('', view=index, name='home'),
]
