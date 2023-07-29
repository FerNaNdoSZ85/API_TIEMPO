import csv

import pandas as pd
import requests

URL_BASE = "https://pokeapi.co/api/v2/pokemon/"

def pokemon_diccionario(content):
    """
    Recibo como parametro las respuestas de la api y
    devuelve un diccionario con las key -> id , nombre ,altura,peso y especie
    """
    poke = dict()
    poke['id'] = content['id']
    poke['nombre'] = content['name']
    poke['altura'] = content['height']  # en decimetros
    poke['peso'] = content['weight']  # en hectogramos
    poke['especie'] = content['types'][0]['type']['name']
    return poke

def cargar_pokemon_list(cantidad=10):
    """ Recibo como parametro la cantidad de pokemon que se quiere consultar en la Api.
    Si no le pasa parametros por defecto solo trae 1
    Devuelve una lista que adentro contiene un diccionario por cada Pokemon
    """
    lista_de_pokemon = list()
    for id_pokemon in range(1, cantidad + 1):

        url = URL_BASE + str(id_pokemon)

        response = requests.get(url)
        codigo_http = response.status_code

        if codigo_http == 200:  # todo OK

            content = response.json()
            pokemon = pokemon_diccionario(content)

            lista_de_pokemon.append(pokemon)

        elif codigo_http == 404: # no existe
            print(f"El pokemon {id_pokemon} NO existe")
        else:  # otro error
            print(f'Ocurrio otro Error. Codigo: {response.status_code}')
        return lista_de_pokemon

print(cargar_pokemon_list(25))

def obtener_df(cant):
    data = cargar_pokemon_list(cant)
    df = pd.DataFrame.from_dict(data)
    return df

print(obtener_df(5))