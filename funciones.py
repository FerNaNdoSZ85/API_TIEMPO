import csv

import pandas as pd
import requests

#! Inicio variables iniciales de manejo
pet_conexion=[]
json_anidados=[]
#! solicitud de conexion al endpoint
def conexion_endpoint(pet_conexion):
    peticion = pet_conexion
    response = requests.get(peticion)
    contenido = response.json()

    #! Verificar el código de estado de la respuesta
    if response.status_code == 200:
        # Mostrar el contenido de la respuesta
        print('*******************')
        print('peticion confirmada')
        print('*******************')
        #! para filtrar en primera instancia--> tomo la lista resultado del JSON
        #dataf = contenido['results'] #! esta variable exporto a scv
        #print("imprimo_dataf_ ")
        df = pd.json_normalize(contenido) #? imprimo esta variable usando json_normalize para que muestre todo en tabla
        json_anidados.append(contenido)
        print(df)
    else:
        print('Error en la solicitud:', response.status_code)

#! defino funcion para la exportacion de variables, filtradas para luego exportar a formato csv
def extraer_variables(json_anidados):
    lista_headers = []
    for data_objets in json_anidados:
        result_dict = {
            "ciudad": data_objets['name'],
            "pais": data_objets['sys']['country'],
            "latitud": data_objets['coord']['lat'],
            "longitud": data_objets['coord']['lon'],
            "temperatura": data_objets['main']['temp'],
            "amanecer": data_objets['sys']['sunrise'],
            "atardecer": data_objets['sys']['sunset'],
            "zona_horaria": data_objets['timezone'],
        }
        lista_headers.append(result_dict)
    return lista_headers

#! defino funcion para exportar las variables a csv
def exportar_csv(lista_variables):
    campos=[]
    a = input("desea exportar al formate scv? S/N: ").upper()
    if a == "S":
        with open ('data.csv', 'w') as file:
            campos = lista_variables[0]
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()
            for i in lista_variables:
                writer.writerow(i)
            print ("-= Exportacion Finalizada =-")
            aas= input("presione ENTER para continuar")
    else:
        aas= input("presione ENTER para continuar")
        pass
