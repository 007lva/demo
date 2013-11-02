from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from models import Patient
import json

def init(req):
    return render_to_response('index.html')

def load(req):
    search = req.GET.get('_search')
    if search == 'true':
        list_patient = filter(req)
    else:
        list_patient = Patient.objects.all()

    list_patient = list(list_patient.values('name','age','weight','size'))

    return HttpResponse(json.dumps(list_patient), content_type='json')

def filter(req):
    searchField = req.GET.get('searchField')
    searchString = req.GET.get('searchString')

    if searchField == 'name':
        list_patient = Patient.objects.filter(name=searchString)
    elif searchField == 'age':
        list_patient = Patient.objects.filter(age=int(searchString))

    return list_patient

@csrf_exempt
def crud(req):
    oper = req.POST.get('oper')

    if oper == 'add':
        add(req)
    elif oper == 'edit':
        edit(req)
    elif oper == 'del':
        delete(req)

    return HttpResponse()

def add(req):
    patient = Patient()
    patient.setReq(req.POST)
    patient.save()

def edit(req):
    idx = req.POST.get('id')
    patient = Patient.objects.get(pk=idx)
    patient.setReq(req.POST)
    patient.save()

def delete(req):
    idx = req.POST.get('id')
    patient = Patient.objects.get(pk=idx)
    patient.delete()