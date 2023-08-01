
import json

import pandas as pd
import requests

from variables import *

#? Cargo el Json de respuesta, y extraigo las variables
archivo = requests.get('https://api.openweathermap.org/data/2.5/forecast?units=metric&cnt=10&lat=31&lon=64&appid=cc3d07bf7909e147cd7443c0415b0f76')
contenido = archivo.json()





