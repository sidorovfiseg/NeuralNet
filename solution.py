from processing import data_processing

from neural_net import NARXModel
from database_work import create_connection
from graphics import print_save_graphic
import os

def run():

    data = create_connection("http://49.12.41.142:8000/get_list/")
    narxmodel = NARXModel()
    narxmodel.learn(data_processing(data))
    print_save_graphic(narxmodel.get_data(), os.getcwd() + "\\resources\\graphics")




