# -*-coding: utf-8

from django.shortcuts import render

# User define module
from .models import RegulationBody

# create your views here


def regulation_text(request):
    r_contents = RegulationBody.objects.all()
    regulation_lines = []

    for e in r_contents:
    #    tmp = [e._id,e._type,e._content]
        tmp = {"id":e._id,"type":e._type,"content":e._contents}
        regulation_lines.append(tmp)



    return render(request,'regulation/regulation_text.html',{'r_contents': regulation_lines})

