from datetime import datetime

import requests
from django.shortcuts import render

from .models import Codigo


# Create your views here.

# method querying sbif service
def request_sbif_service(date_into):
    date = datetime.strptime(date_into, "%Y-%m-%d").date()
    month = date.month
    year = date.year
    if date.day < 15:
        month = month - 1
        if month == 0:
            year = year - 1
            month = 12
    try:
        response = requests.get(
            'https://api.sbif.cl/api-sbifv3/recursos_api/tmc/{m}/{d}?apikey=9c84db4d447c80c74961a72245371245cb7ac15f&formato=json'.format(
                m=year, d=month))
        return response.json()
    except Exception:
        return {"CodigoHTTP": 404, "Mensaje": "Error al consultar Servicio"}


# Compare Conditions, returning a true or false
def condition_value(condition, value_joined, value_compare):
    if condition == 'Menor que':
        return value_joined < value_compare
    if condition == 'Mayor que':
        return value_joined > value_compare
    if condition == 'Mayor igual':
        return value_joined >= value_compare
    if condition == 'Menor igual':
        return value_joined <= value_compare
    if condition == 'Igual que':
        return value_joined == value_compare


# method goes through the list of rules to be followed
def valida_condition(condition, entry, type):
    if condition is None:
        return True
    for x in condition:
        if type == 'dias':
            attribute = x.dias
        else:
            attribute = x.uf
        compare = condition_value(x.condicion, entry, attribute)
        if not compare:
            return False
    return True


# method that validates data entered from the form
def valid_request(request):
    error=[]
    try:
        if int(request.POST['plazo']) <= 0:
            error.append("Dias de atraso.")
    except ValueError:
        error.append("Dias de atraso.")
    try:
        datetime.strptime(request.POST['fecha'], "%Y-%m-%d").date()
    except ValueError:
        error.append("Fecha.")
    try:
        new_float = float(request.POST['uf'])
        if new_float <= 0:
            error.append("Valor UF.")
    except ValueError:
        error.append("Valor UF.")
    if error is None:
        return None
    texto = "Los siguientes campos tienen errores: "
    for x in error:
        texto = texto+" "+ x
    return message_error(texto)

def valid_code(cod, exampleRadios):
    if exampleRadios == 'option1':
        return cod.reajustable
    if exampleRadios == 'option2':
        return not cod.reajustable
    if exampleRadios == 'option3':
        return True


# method that compares sbif listing and values ​​entered by the user
def compare_data(req, request):
    lista_final = []
    list_tipos = []
    for x in req.get('TMCs'):
        list_tipos.append(int(x.get('Tipo')))
    list_code_db = Codigo.objects.filter(codigo__in=list_tipos)
    for y in list_code_db:
        if valid_code(y, request.POST['exampleRadios']):
            if valida_condition(y.dia_set.filter(codigo_id=y.id), int(request.POST['plazo']),'dias') \
                    and valida_condition(y.uf_set.filter(codigo_id=y.id), float(request.POST['uf']),'uf'):
                lista_final.append(search(req.get('TMCs'),y))
    return lista_final


def search(list, object):
    for x in list:
        if int(x.get('Tipo')) == object.codigo:
            return x

def message_error(text):
    return {"Mensaje": text}


def response_object(att, request):
    return {'error': att.get('Mensaje'), 'request': request_object(request)}

def request_object(request):
    return {
        'plazo': request.POST['plazo'],
        'fecha': request.POST['fecha'],
        'uf': request.POST['uf'],
        'select': request.POST['exampleRadios']
    }


# internal method orchestrator
def app_sbif(request):
    att = valid_request(request)
    if att is not None:
        return render(request, 'base.html', response_object(att, request))
    try:
        req = request_sbif_service(request.POST['fecha'])
        if req.get('CodigoHTTP') is not None:
            return render(request, 'base.html', response_object(req, request))
        lista_final = compare_data(req, request)
        if not lista_final:
            lista_final.append({"Titulo": "No se encontraron datos", "SubTitulo": "", "Valor": "Sin datos"})
            return render(request, 'base.html', {'result': lista_final, 'request': request_object(request)})
        return render(request, 'base.html', {'result': lista_final, 'request': request_object(request)})
    except Exception:
        return render(request, 'base.html', response_object(message_error("Se produjo un error en la solicitud"), request))

# initial method
def init_page(request):
    if request.method == 'POST':
        return app_sbif(request)
    else:
        return render(request, 'base.html',{'request': {'select': 'option3'}})
