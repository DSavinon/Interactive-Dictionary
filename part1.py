import json
import string
from difflib import get_close_matches

data = json.load(open("data.json"))
data = {k.title(): v for k, v in data.items()}
# print(data.keys())
palabra = input("Ingresa una Palabra: ")


def get_value(llave: string):
    """Recibimos una llave por input y regresamos el valor

    Args:
        llave (string): Llave en el diccionario
    """

    llave = llave.title()
    if llave.title() not in data:
        palabra_corregida = get_close_matches(llave, data, cutoff=0.7)
        if len(palabra_corregida) > 0:
            print(f"Mostrando Resultados de: {palabra_corregida[0]}")
            return data[palabra_corregida[0]]
        else:
            return f"{llave} No existe en el diccionario"
    else:
        return data[llave]


resultado = get_value(palabra)
# print(f"Tipo: {type(resultado)}")
if type(resultado) == list:
    for r in resultado:
        print("Significado: ", r)
else:
    print(resultado)
