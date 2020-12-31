# -*- coding: utf-8 -*-

import numpy as np

class PulseGenerator:
    def __init__(self, sampling_freq:int):
        self.sampling_freq = sampling_freq

    def generate(self, freq:float, length:float) -> np.array:
        period = self.sampling_freq/freq
        output = np.zeros(self.sampling_freq*length)
        for i in range((int)(self.sampling_freq*length/period)):
            output[(int)(i*period)] = 1
        return output
