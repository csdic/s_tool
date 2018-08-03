from django.shortcuts import render


# create your views here

def regulation_text(request):
    return render(request, 'regulation/regulation_text.html', {})

