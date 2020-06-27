from datetime import datetime

import requests
from django.shortcuts import render

# Create your views here.
from tmc_app.reglas import LISTADO_REGLAS, LISTADO_CODIGO_NO_REAJUSTABLE, LISTADO_CODIGO_REAJUSTABLE


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
        compare = condition_value(x.get('condicion'), entry, x.get(type))
        if not compare:
            return False
    return True


# method that validates data entered from the form
def valid_request(request):
    if int(request.POST['plazo']) <= 0:
        return message_error("Dias de atraso incorrecto.")
    try:
        datetime.strptime(request.POST['fecha'], "%Y-%m-%d").date()
    except ValueError:
        return message_error("Fecha ingresada incorrecta.")
    try:
        new_float = float(request.POST['uf'])
        if new_float <= 0:
            return message_error("Valor UF no valido.")
    except ValueError:
        return message_error("Valor UF no valido.")
    return None


def valid_code(cod, exampleRadios):
    if exampleRadios == 'option1':
        return cod in LISTADO_CODIGO_REAJUSTABLE
    if exampleRadios == 'option2':
        return cod in LISTADO_CODIGO_NO_REAJUSTABLE
    if exampleRadios == 'option3':
        return True


# method that compares sbif listing and values ​​entered by the user
def compare_data(req, request):
    lista_final = []
    mapRegla = LISTADO_REGLAS
    for x in req.get('TMCs'):
        for y in mapRegla:
            if x.get('Tipo') == y.get('codigo') and valid_code(int(x.get('Tipo')), request.POST['exampleRadios']):
                if valida_condition(y.get('dia'), int(request.POST['plazo']), 'dias') \
                        and valida_condition(y.get('uf'), float(request.POST['uf']), 'uf'):
                    lista_final.append(x)
    return lista_final


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
    req = request_sbif_service(request.POST['fecha'])
    if req.get('CodigoHTTP') is not None:
        return render(request, 'base.html', response_object(req, request))
    lista_final = compare_data(req, request)
    if not lista_final:
        lista_final.append({"Titulo": "No se encontraron datos", "SubTitulo": "", "Valor": "Sin datos"})
        return render(request, 'base.html', {'result': lista_final, 'request': request_object(request)})
    return render(request, 'base.html', {'result': lista_final, 'request': request_object(request)})


# initial method
def init_page(request):
    if request.method == 'POST':
        return app_sbif(request)
    else:
        return render(request, 'base.html',{'request': {'select': 'option3'}})
