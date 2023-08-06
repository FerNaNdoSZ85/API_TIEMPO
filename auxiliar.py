import json

import pandas as pd

file = open('F:\API_WEATHER_DA\API_TIEMPO_FORECAST\json_total.json',)

datos_clima = json.load(file) # json puro respuestafull
dataf = pd.DataFrame(datos_clima)
#print (dataf)
ciudades ={}
valores ={}
valor_3hr=[]

cont=0
def extraer_3hr(datos_clima):
    valores ={}
    valor_3hr=[]
    for i in datos_clima: # este es el json_anidado cargado
        ciudades['ciudad'] = i['city']['name']
        ciudades['latitud'] = i['city']['coord']['lat']
        ciudades['longitud'] = i['city']['coord']['lon']
        ciudades['amanecer'] = i['city']['sunrise']
        
        for j in i['list']: #? debo realizar 40 eperaciones dentro del mismo ciclo con un cambio de variable
            valores['temp'] = j['main']['temp'] #? j <==> i['list'] sigue sin funcionar
            valores['temp_min'] = j['main']['temp_min']
            valor_3hr.append(valores)
            ciudades['valores'] = valor_3hr
            print(j)

        with open(f"{i['city']['name']}.json", 'w') as jf:
            json.dump(ciudades, jf, ensure_ascii=False, indent=2)
        valores ={}
        valor_3hr=[]

extraer_3hr(datos_clima)