import csv

# en el archivo de configs voy a guardar los datos sensibles
from configs import BASE_URL, token2

#? Lista de las ciudades para el endpoint
cityList= ["London", "New%20York", "Cordoba", "Taipei", "Buenos%20Aires",
            "Mexico%20City", "Dublin", "Tiflis", "Bogota", "Tokio"]

#? Coordenadas de las ciudades
coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64",
                "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99",
                "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74",
                "lat=35&lon=139"]

#? Defino una funcion para concatenar la BASE_URL, con las coordenadas y el token
lista_urls=[]
def consultas_url ():
    for c in range(10):
        lista_urls.append(BASE_URL + coordList[c]+'&appid='+token2)
    return lista_urls

#? defino exportacion de csv


#print(json_anidados)
#df2 = pd.json_normalize(json_anidados)
#print("imprimo df2")
#print(df2)

#print("imprimo lista url de las ciudades")
#for i in lista_urls:
#    print(i)

"""print("imprimo JSON_ANIDADOS")
for j in json_anidados:
    print(j.keys())
    a=list(j.keys())
#print(a)
print(json_anidados[0]['coord'])"""