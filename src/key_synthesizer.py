# -*- coding: utf-8 -*-

import numpy as np

from blade import Blade
from grain import Grain

class KeySynthesizer:
    def __init__(self, sampling_freq:int, freq:float):
        self.sampling_freq = sampling_freq
        self.freq = freq
        self.period = sampling_freq / freq
        self.is_active = False
        self.blade = Blade(sampling_freq, Grain(sampling_freq, 50))
        self.last_blade_idx = -self.period
        self.bufor = np.zeros(0)

    def start(self):
        self.is_active = True

    def stop(self):
        self.is_active = False
        self.last_blade_idx = -self.period

    def get_chunk(self, chunk_size:int) -> np.array:
        if self.is_active:
            while self.last_blade_idx + self.period < chunk_size:
                next_blade_start = int(self.last_blade_idx + self.period)
                next_blade = self.blade.get_vector()
                self.bufor = np.concatenate([
                    self.bufor,
                    np.zeros(next_blade_start + next_blade.size - self.bufor.size)
                ])
                self.bufor[next_blade_start : next_blade_start + next_blade.size] += next_blade
                self.last_blade_idx += self.period
            self.last_blade_idx -= chunk_size
        elif self.bufor.size == 0:
            return np.zeros(chunk_size)
        elif self.bufor.size < chunk_size:
            self.bufor = np.concatenate([
                self.bufor,
                np.zeros(chunk_size - self.bufor.size)
            ])
        output = self.bufor[:chunk_size]
        self.bufor = self.bufor[chunk_size:]
        return output
