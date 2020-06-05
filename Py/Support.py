import numpy as np


class Ave:

    def __init__(self, data):
        self.data = data

    def get_ave(self):
        return np.average(self.data)
