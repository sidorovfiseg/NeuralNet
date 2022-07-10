import pandas as pd
import psycopg2
from psycopg2 import OperationalError
import localdata_read as ldr
import requests
import os

import requests.exceptions as ex

# Function which create connection with postgreSQL
# Функция, которая создает подключение к postgreSQL


def create_connection(api_url):
    connection = None
    try:
        responce = requests.get(api_url)
        jsn = responce.json()
        print("Connection is success")
        return read_data_from_json(jsn)
    except ex.ConnectionError as e:
        print(f"Connection error occurred, using local data.csv")
        path = os.getcwd() + "\\resources\\data.csv"
        return ldr.read_data_from_csv(path)


# Парсинг json

def read_data_from_json(jsn):
    source_address = []
    humidity = []
    sound_level = []
    light_level = []
    uv_index = []
    pressure = []
    eco2 = []
    magnetic = []
    temperature = []

    for i in range(0, 3000):
        source_address.append(jsn[i]['source_address'])
        humidity.append(jsn[i]['humidity'])
        sound_level.append(jsn[i]['sound_level'])
        light_level.append(jsn[i]['light_level'])
        uv_index.append(jsn[i]['uv_index'])
        pressure.append(jsn[i]['pressure'])
        eco2.append(jsn[i]['eco2'])
        magnetic.append(jsn[i]['magnetic'])
        temperature.append(jsn[i]['temperature'])

    source_address = pd.DataFrame(source_address, columns=['source_address'])
    humidity = pd.DataFrame(humidity, columns=['humidity'])
    sound_level = pd.DataFrame(sound_level, columns=['sound_level'])
    light_level = pd.DataFrame(light_level, columns=['light_level'])
    uv_index = pd.DataFrame(uv_index, columns=['uv_index'])
    pressure = pd.DataFrame(pressure, columns=['pressure'])
    eco2 = pd.DataFrame(eco2, columns=['eco2'])
    magnetic = pd.DataFrame(magnetic, columns=['magnetic'])
    temperature = pd.DataFrame(temperature, columns=['temperature'])

    x = pd.concat([source_address, humidity, sound_level, light_level,
                   uv_index, pressure, eco2, magnetic], axis=1)
    y = pd.concat([temperature], axis=1)

    return [x, y]


