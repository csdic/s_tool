from django.shortcuts import render

# User define module
from .models import RegulationBody

# create your views here

def regulation_text(request):
    r_contents = RegulationBody.objects.all()
    return render(request, 'regulation/regulation_text.html', {'r_contents':r_contents})

