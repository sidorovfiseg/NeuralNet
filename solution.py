from processing import data_processing

import database_work
from neural_net import NARXModel
from database_work import create_connection
from graphics import print_save_graphic
import json

def run():

    data = create_connection("http://49.12.41.142:8000/get_list/")
    narxmodel = NARXModel()
    narxmodel.learn(data_processing(data))
    print_save_graphic(narxmodel.get_data(), "resources/graphics.png")




