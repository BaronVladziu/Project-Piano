# -*- coding: utf-8 -*-

import numpy as np

class Blade:
    def __init__(self, sampling_freq:int, grain:"Grain"):
        self.sampling_freq = sampling_freq
        self.grain = grain

    def get_vector(self) -> np.array:
        return self.grain.get_vector()
