import pandas as pd

from funciones import *
from variables import *


#! defino funcion inicial para realizar las request
def clima_ciudades():
    consultas_url()
    for c in range(10):
        pet_conexion=lista_urls[c]
        conexion_endpoint(pet_conexion)

clima_ciudades()

# Obtener la lista de diccionarios con las variables extraídas
lista_variables = extraer_variables(json_anidados)
text = pd.json_normalize(lista_variables)

# Imprimir la lista de diccionarios resultante
#print(text)

#! llamo la funcion exportar
exportar_csv(lista_variables)

