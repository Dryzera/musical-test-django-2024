from django.shortcuts import render
from django.views.generic import ListView
from main.models import UserPerfil

# Only tests
def index(request):
    return render(request, template_name='home.html')

class SearchProfiles(ListView):
    model = UserPerfil
    template_name = 'search_profiles.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return UserPerfil.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = self.get_queryset()
        return context
