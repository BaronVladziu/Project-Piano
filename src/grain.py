# -*- coding: utf-8 -*-

import numpy as np

from biquad import Biquad

def gaussian(x, m, sd):
    return np.exp(-np.power(x - m, 2.) / (2 * np.power(sd, 2.)))

class Grain:
    def __init__(self, sampling_freq:int, length_ms:float):
        self.sampling_freq = sampling_freq
        self.length_ms = length_ms
        self.length = int(length_ms * sampling_freq / 1000)

        self.filters = list()
        for filter_nr in range(1):
            self.filters.append(Biquad())
            self.filters[filter_nr].randomize_params()

        self.sd = 0.001
        inside_signal = np.random.normal(0, 1, int(self.length))
        for filter in self.filters:
            inside_signal = filter.filter(inside_signal)
        self.vector = inside_signal \
            * gaussian(
                np.arange(start=0, stop=self.length),
                self.length/2,
                self.sd*self.sampling_freq
            )
        # self.vector = np.zeros(self.length)
        # self.vector[0] = 1.0
    
    def get_vector(self) -> np.array:
        return self.vector
