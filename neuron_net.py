import random

import numpy as np
from pyneurgen.neuralnet import NeuralNet
from pyneurgen.recurrent import NARXRecurrent


class NARXModel:
    # Конструктор
    def __init__(self):
        self.model = NeuralNet()

    # инициализируем слои, задаем параметры в NARXRecurent
    def _init_layers(self, input_nodes, hidden_nodes, output_nodes,
                     output_order, incoming_weight_from_output,
                     input_order, incoming_weight_from_input):
        random.seed(2016)
        self.model.init_layers(input_nodes,
                               [hidden_nodes],
                               output_nodes,
                               NARXRecurrent(output_order,
                                             incoming_weight_from_output,
                                             input_order,
                                             incoming_weight_from_input)
                               )
        self.model.randomize_network()
        self.model.layers[1].set_activation_type('sigmoid')

    # Загружаем данные, устанавливаем рамки для обучения
    def _setting(self, learn_rate, x, y, learn_end):
        self.model.set_learnrate(learn_rate)
        self.model.set_all_inputs(x)
        self.model.set_all_targets(y)
        self.model.set_learn_range(0, learn_end)
        self.model.set_test_range(learn_end + 1, len(x) - 1)

    # собираем все вместе и обучаем
    def learn(self, data):
        self._init_layers(8, 14, 1, 1, 0.8, 3, 0.5)
        self._setting(0.35, data[0], data[1], int(len(data[0]) * 0.85))
        self.model.learn(epochs=100, show_epoch_results=True, random_testing=False)
        mse = self.model.test()

    # получения массива prediction и target
    def get_data(self):
        target_and_prediction = [np.array([item[0][0] for item in self.model.test_targets_activations]),
                                 np.array([item[1][0] for item in self.model.test_targets_activations])]
        return target_and_prediction
