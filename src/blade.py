# -*- coding: utf-8 -*-

import numpy as np

class Blade:
    def __init__(self, sampling_freq:int, grain:"Grain", positions:list):
        self.sampling_freq = sampling_freq
        self.grain = grain
        self.positions = positions        

    def get_vector(self) -> np.array:
        grain_vector = self.grain.get_vector()
        blade_vector = np.zeros(int(self.positions[-1]*self.sampling_freq/1000) + grain_vector.size)
        for pos in self.positions:
            blade_vector[int(pos*self.sampling_freq/1000):int(pos*self.sampling_freq/1000) + grain_vector.size] += grain_vector
        return blade_vector
