# -*- coding: utf-8 -*-

import numpy as np

class Grain:
    def __init__(self, sampling_freq:int, length_ms:float):
        self.sampling_freq = sampling_freq
        self.length_ms = length_ms
        self.length = int(length_ms * sampling_freq / 1000)
    
    def get_vector(self) -> np.array:
        vector = np.zeros(self.length)
        vector[0] = 1.0
        return vector
