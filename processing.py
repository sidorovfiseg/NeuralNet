import  pandas as pd
from sklearn import preprocessing
import  numpy as np
# Обработка данных

fitter = preprocessing.MinMaxScaler(feature_range=(0, 1))

def data_processing(data):
    processed_data = []
    for data_i in data:
        data_i = data_i.astype(float)
        data_i = np.array(data_i).reshape((len(data_i), len(data_i.columns)))
        data_i = fitter.fit_transform(data_i)
        processed_data.append(data_i.tolist())

    return processed_data

