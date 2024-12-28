from django.shortcuts import render
from django.views.generic import ListView
from main.models import UserPerfil, Localidade, User
from django.db.models import Q


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
        context['localidades'] = Localidade.objects.all()
        return context
    
    def post(self, *args, **kwargs):
        filter_options = {}
        query_set_list = []

        filter_options['name_user'] = self.request.POST.get('name-user')
        filter_options['localidade'] = self.request.POST.get('localidade')
        filter_options['categoria'] = self.request.POST.get('categoria')
        filter_options['cargo'] = self.request.POST.get('cargo')

        # add logic for compare query sets and not send values equals
        
        if filter_options['name_user']:
            user = User.objects.filter(
                Q(username__icontains=filter_options['name_user']) |
                Q(first_name__icontains=filter_options['name_user'])
            )
            for i in user:
                user_account = UserPerfil.objects.filter(user=i)
                query_set_list.append(user_account)

        if filter_options['localidade'] != 'None':
            user_localidade = UserPerfil.objects.filter(localidade=filter_options['localidade'])
            query_set_list.append(user_localidade if user_localidade not in query_set_list else ...) 

        if filter_options['categoria'] != 'None':
            user_categoria = UserPerfil.objects.filter(categoria__icontains=filter_options['categoria'])
            query_set_list.append(user_categoria if user_categoria not in query_set_list else ...)

        if filter_options['cargo'] != 'None':
            user_cargo = UserPerfil.objects.filter(grupo=filter_options['cargo'])
            query_set_list.append(user_cargo if user_cargo not in query_set_list else ...)

        print(query_set_list)
        return render(self.request, self.template_name, context={'list_match_users': query_set_list})
