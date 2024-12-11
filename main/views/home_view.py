from django.shortcuts import render

# Create your views here.


# Only tests
def index(request):
    return render(request, template_name='home.html')