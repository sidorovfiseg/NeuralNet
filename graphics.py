import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from processing import fitter
# рисуем и сохраняем графики


def print_save_graphic(target_and_prediction, path):
    plt.figure(figsize=(10, 10))
    plt.subplot(2, 1, 1)
    plt.plot(fitter.inverse_transform(pd.DataFrame(target_and_prediction[0])))
    plt.plot(fitter.inverse_transform(pd.DataFrame(target_and_prediction[1])))
    plt.legend(['target', 'prediction'])
    plt.subplot(2, 1, 2)
    plt.plot(
        abs(fitter.inverse_transform(pd.DataFrame(target_and_prediction[0])) -
            fitter.inverse_transform(pd.DataFrame(target_and_prediction[1]))))
    plt.legend(['error'])
    plt.show()
    plt.savefig(path)
