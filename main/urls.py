from django.contrib import admin
from django.urls import path, include
from .views import index

app_name = 'main'

urlpatterns = [
    # perfil urls
    path('perfil/<int:pk>/resumegames/', view=index, name='resumegames'),
    path('perfil/<int:pk>/', view=index, name='perfil'),

    # game urls
    path('game/', view=index, name='game'),
    path('game/resume/', view=index, name='game_resume'),
    path('games/', view=index, name='games'),

    # generic urls
    path('search/<slug:slug>/', view=index, name='search'),
    path('', view=index, name='home'),
]
