# -*-coding: utf-8

from django.shortcuts import render

# User define module
from .models import RegulationBody

# create your views here


def regulation_text(request):
    r_contents = RegulationBody.objects.all()
    regulation_lines = []
    section_type: int = 0; # type 0 means contents, 1 means h1, 2 means 2, ...
    for e in r_contents:
         if e._type == "section_title":
            s_line = e._content.split(' ')
            num = s_line[0].split('.')
            section_type = len(num)

        tmp = {"id":e._id,"type":section_type,"content":e._content}
        regulation_lines.append(tmp)

    return render(request,'regulation/regulation_text.html',{'r_contents': regulation_lines})

