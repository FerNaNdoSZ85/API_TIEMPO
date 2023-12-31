import csv
import json

import pandas as pd
import requests

from conex_db import *

#! Inicio variables iniciales de manejo
pet_conexion=[]
json_anidados=[]
valor_3hr=[]
datos_clima = {}
valores_diarios ={}
ciudades ={}
datos_csv = {} # variable en la que voy almacenar todas las peticiones
#! solicitud de conexion al endpoint
def conexion_endpoint(pet_conexion):
    peticion = pet_conexion
    response = requests.get(peticion)
    print(response.status_code)
    contenido = response.json()

    #! Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # Mostrar el contenido de la respuesta
        print('*******************')
        print('peticion confirmada')
        print('*******************')
        #! para filtrar en primera instancia--> tomo la lista resultado del JSON
        #df = pd.json_normalize(contenido)   #? imprimo esta variable usando json_normalize para que muestre todo en tabla
        json_anidados.append(contenido)     #! de aqui extraigo los campos que necesito
        #print(json_anidados)
        extraer_datos(json_anidados)
        with open(f"json_total.json", 'w') as jf:
            json.dump(json_anidados, jf, ensure_ascii=False, indent=2)
    else:
        print('Error en la solicitud:', response.status_code)
    return(json_anidados)

def extraer_datos(json_anidados):
    for datos in json_anidados:
        valor_3hr=[]
        datos_clima={}
        ciudades[datos['city']['name']] = datos_clima #! en esta variable almaceno todas las respuestas
        datos_clima['ciudad']=datos['city']['name']
        datos_clima['pais']=datos['city']['country']
        datos_clima['zona_horaria']=datos['city']['timezone']
        datos_clima['latitud']=datos['city']['coord']['lat']
        datos_clima['longitud']=datos['city']['coord']['lon']
        datos_clima['amanecer']=datos['city']['sunrise']
        datos_clima['atardecer']=datos['city']['sunset']

        #? para extraer los valores diarios, genero una nueva funcion y variable en la cual voy a recorrer "list"
        #? e ir almacenando en un nuevo diccionario
        for v in datos['list']:
            valores_diarios['dt'] = v['dt']
            valores_diarios['temperatura'] = v['main']['temp']
            valores_diarios['temp_min'] = v['main']['temp_min']
            valores_diarios['temp_max'] = v['main']['temp_max']
            valores_diarios['estado'] = v['weather'][0]['main']
            valores_diarios['dt_txt'] = v['dt_txt']
            valor_3hr.append(valores_diarios) # realizar verificacion en estas lineas: anidacion erronea
        datos_clima['valores_diarios'] = valor_3hr
        
        datos_csv.update(datos_clima)

        with open(f"{datos['city']['name']}.json", 'w') as jf:
            json.dump(ciudades, jf, ensure_ascii=False, indent=2)

        valor_3hr=[]
        datos_clima={}
        #print(type(datos_csv))
        with open(f"datos_csv.json", 'w') as dcsv:
            json.dump(datos_csv, dcsv, ensure_ascii=False, indent=2)
    return datos_csv



def exportar_csv(datos_csv): #! estas mi variabla de exportacion para csv
    a= input('Exportar formato csv: SI o NO: ').upper()
    if a == 'S':
        campos=list(datos_csv.keys()) + list(datos_csv['valores_diarios'][0]) #? Extraigo del diccionario los headers

        with open('datos_csv.csv', 'w') as fcsv:
            writer = csv.DictWriter(fcsv, fieldnames=campos)
            writer.writeheader()
            for t in datos_csv['valores_diarios']:
                writer.writerow(t)
            print ("-= Exportacion Finalizada =-")
            aas= input("presione ENTER para continuar")
    else:
        aas= input("presione ENTER para continuar")
        pass





