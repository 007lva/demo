from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
#REVISAR:
#from django.core import serializers

def home(req):
    return render_to_response('index.html', {"papi":"luigi"})

def ajax(req):
    lista = []
    persona1 = {"nombre":"luigi","edad":25}
    persona2 = {"nombre":"jose","edad":26}
    lista.append(persona1)
    lista.append(persona2)
    lista_json = json.dumps(lista)
    return HttpResponse(lista_json, content_type='json')