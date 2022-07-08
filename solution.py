from processing import data_processing
from neural_net import NARXModel
from database_work import create_connection
from graphics import print_save_graphic


def run():
    data = create_connection()
    narxmodel = NARXModel()
    narxmodel.learn(data_processing(data))
    print_save_graphic(narxmodel.get_data(), "resources/graphics.png")




