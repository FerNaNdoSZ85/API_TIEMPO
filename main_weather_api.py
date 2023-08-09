
from conex_db import *
from funciones import *
from variables import *


#! defino funcion inicial para realizar las request
def clima_ciudades():
    consultas_url()
    for c in range(2):
        pet_conexion=lista_urls[c]
        conexion_endpoint(pet_conexion)

clima_ciudades()
exportar_csv(datos_csv)
carga_datos()