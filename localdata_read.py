import pandas as pd

# Читаем нужные данные из csv


def read_data_from_csv(path, delimiter=";"):
    data = pd.read_csv(path, delimiter)
    source_address = data["source_address"]
    humidity = data["humidity"]
    sound_level = data["sound_level"]
    light_level = data["light_level"]
    uv_index = data["uv_index"]
    pressure = data["pressure"]
    eco2 = data["eco2"]
    magnetic = data["magnetic"]
    temperature = data["temperature"]
    x = pd.concat([source_address, humidity, sound_level, light_level,
                   uv_index, pressure, eco2, magnetic], axis=1)
    y = pd.concat([temperature], axis=1)
    return [x, y]

