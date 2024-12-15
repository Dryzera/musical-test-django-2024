from django.contrib import admin
from .models import Perguntas, PerguntasJogo, Localidade, UserPerfil, Jogo, Respostas

# Register your models here.

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at',)
    readonly_fields = ('created_at', 'finished_at')

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
