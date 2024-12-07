from django.contrib import admin
from .models import Perguntas, PerguntasJogo, Localidade, UserPerfil, Jogo, Respostas

# Register your models here.

admin.site.register(Jogo)
admin.site.register(Localidade)
admin.site.register(UserPerfil)
admin.site.register(PerguntasJogo)

class RespostasAdmin(admin.TabularInline):
    model = Respostas
    extra = 2

@admin.register(Perguntas)
class PerguntasAdmin(admin.ModelAdmin):
    inlines = [RespostasAdmin,]
    list_display = ('pergunta', 'fase', 'dificuldade')
