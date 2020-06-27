
LISTADO_REGLAS = [
    {
        'codigo': '1', 'dia': None,
        'uf': None
    },
    {
        'codigo': '2', 'dia': [{'dias': 90, 'condicion': 'Menor que'}],
        'uf': None
    },
    {
        'codigo': '3', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': None
    },
    {
        'codigo': '4', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 100, 'condicion': 'Menor igual'}]
    },
    {
        'codigo': '5', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 200, 'condicion': 'Menor igual'},{'uf': 100, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '6', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 200, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '7', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 200, 'condicion': 'Menor igual'}]
    },
    {
        'codigo': '8', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 5000, 'condicion': 'Menor igual'},{'uf': 200, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '9', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 5000, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '10', 'dia': [{'dias': 90, 'condicion': 'Menor que'}],
        'uf': [{'uf': 5000, 'condicion': 'Menor que'}]
    },
    {
        'codigo': '11', 'dia': [{'dias': 90, 'condicion': 'Menor que'}],
        'uf': [{'uf': 5000, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '12', 'dia': [{'dias': 365, 'condicion': 'Menor que'}],
        'uf': None
    },
    {
        'codigo': '13', 'dia': [{'dias': 365, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 2000, 'condicion': 'Menor igual'}]
    },
    {
        'codigo': '14', 'dia': [{'dias': 365, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 2000, 'condicion': 'Mayor que'}]
    }
    ,{
        'codigo': '15', 'dia': None,
        'uf': None
    },
    {
        'codigo': '20', 'dia': [{'dias': 365, 'condicion': 'Mayor igual'}],
        'uf': None
    },
    {
        'codigo': '21', 'dia': [{'dias': 365, 'condicion': 'Menor que'}],
        'uf': None
    },
    {
        'codigo': '22', 'dia': [{'dias': 365, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 2000, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '23', 'dia': [{'dias': 365, 'condicion': 'Mayor igual'}],
        'uf': None
    },
    {
        'codigo': '24', 'dia': [{'dias': 365, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 2000, 'condicion': 'Menor igual'}]
    },
    {
        'codigo': '25', 'dia': [{'dias': 90, 'condicion': 'Menor que'}],
        'uf': [{'uf': 5000, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '26', 'dia': [{'dias': 90, 'condicion': 'Menor que'}],
        'uf': [{'uf': 5000, 'condicion': 'Menor igual'}]
    },
    {
        'codigo': '27', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 5000, 'condicion': 'Menor igual'},{'uf': 200, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '28', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 100, 'condicion': 'Menor igual'}]
    },
    {
        'codigo': '29', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 5000, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '30', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 200, 'condicion': 'Menor igual'}]
    },
    {
        'codigo': '31', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 200, 'condicion': 'Menor igual'},{'uf': 100, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '32', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 200, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '33', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 200, 'condicion': 'Menor igual'}]
    },
    {
        'codigo': '34', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 5000, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '35', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 5000, 'condicion': 'Menor igual'},{'uf': 200, 'condicion': 'Mayor que'}]
    },
    #    {
    #   'codigo': '36', 'dia': None,
#   'uf': None
    #   },
    {
        'codigo': '37', 'dia': [{'dias': 90, 'condicion': 'Menor que'}],
        'uf': None
    },
    # {
    #    'codigo': '38', 'dia': None,
#    'uf': None
    #    },
    {
        'codigo': '39', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': None
    },
     {
        'codigo': '40', 'dia': None,
        'uf': None
     },
    #  {
    #    'codigo': '41', 'dia': None,
#     'uf': [{'uf': 2000, 'condicion': 'Menor igual'}]
    # },
    #  {
    #    'codigo': '42', 'dia': None,
#     'uf': [{'uf': 2000, 'condicion': 'Mayor que'}]
#  },
     #{
    #   'codigo': '43', 'dia': None,
#   'uf': None
    # },
    {
        'codigo': '44', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 200, 'condicion': 'Menor igual'},{'uf': 50, 'condicion': 'Mayor que'}]
    },
    {
        'codigo': '45', 'dia': [{'dias': 90, 'condicion': 'Mayor igual'}],
        'uf': [{'uf': 50, 'condicion': 'Menor igual'}]
    }
]