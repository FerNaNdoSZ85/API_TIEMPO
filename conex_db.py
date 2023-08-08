
import pandas as pd
import psycopg2 as pg2
from sqlalchemy import create_engine


def carga_datos():
    try:
        #? Leer archivo csv exportado
        csv_datos = "F:\API_WEATHER_DA\API_TIEMPO_FORECAST\datos_csv.csv"
        dataframe =pd.read_csv(csv_datos)

        #?conexion con base de datos
        conexion = pg2.connect(database = 'forecast',
                        user = 'postgres',
                        password = 'StoneZ333333',
                        host = 'localhost',
                        port ='5432')
        conexion.autocommit = True

        #? gestor de base sqlalchemy
        engine = create_engine('postgresql+psycopg2://postgres:StoneZ333333@localhost:5432/forecast', pool_pre_ping=True)

        #? envio de datos CSV a base de sqlalchemy
        table_name = "datos_climaticos"
        dataframe.to_sql(table_name, engine, if_exists='replace', index=True)

        print ( "-=!! CARGA EXITOSA DE DATOS !!=-- ")
    except Exception:
        print("Error en la conexion")




