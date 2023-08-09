
import pandas as pd
import psycopg2 as pg2
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:StoneZ333333@localhost:5432/forecast')

def carga_datos():
    try:
        #?conexion con base de datos
        conexion = pg2.connect(database = 'forecast',
                        user = 'postgres',
                        password = 'StoneZ333333',
                        host = 'localhost',
                        port ='5432')

        #? gestor de base sqlalchemy
        
        conexion.autocommit = True

        #? Leer archivo csv exportado
        csv_datos = "F:\API_WEATHER_DA\API_TIEMPO_FORECAST\datos_csv.csv"
        dataframe =pd.read_csv(csv_datos)

        #? envio de datos CSV a base de sqlalchemy
        table_name = "datos_climaticos"
        dataframe.to_sql(table_name, engine, if_exists='replace', index=True)

        print ( "-=!! CARGA EXITOSA DE DATOS !!=-- ")
    except Exception as ex:
        print('ERROR??')
