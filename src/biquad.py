# -*- coding: utf-8 -*-

import random
import numpy as np

class Biquad:
    def __init__(self):
        self.K = 1.0
        self.b0 = 1.0
        self.b1 = 0.0
        self.b2 = 0.0
        self.a1 = 0.0
        self.a2 = 0.0

        self.x0 = 0.0
        self.x1 = 0.0
        self.x2 = 0.0
        self.y0 = 0.0
        self.y1 = 0.0
        self.y2 = 0.0

    def check_stability(self):
        if self.a1*self.a1 - 4*self.a2 >= 0:
            raise AttributeError("ERROR: Biquad filter is not stable!")
        if self.a1*self.a1 - 2*self.a2 >= 2:
            raise AttributeError("ERROR: Biquad filter is not stable!")

    def set_params(self,
        K:float, b0:float, b1:float, b2:float,
        a1:float, a2:float
    ):
        self.K = K
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.a1 = a1
        self.a2 = a2
        self.check_stability()

    def randomize_params(self):
        if_stable = False
        while not if_stable:
            try :
                self.a1 = random.uniform(-2.0, 2.0)
                self.a2 = random.uniform(-1.0, 1.0)
                self.check_stability()
                if_stable = True
            except AttributeError:
                if_stable = False

        self.b0 = random.uniform(-1.0, 1.0)
        self.b1 = random.uniform(-1.0, 1.0)
        self.b2 = random.uniform(-1.0, 1.0)
        self.K = 1/(np.abs(self.b0) + np.abs(self.b1) + np.abs(self.b2) + np.abs(self.a1) + np.abs(self.a2))

    def filter(self, signal:"numpy.array") -> "numpy.array":
        signal = np.concatenate([signal, [0.0, 0.0]])
        output = np.zeros(signal.size)
        for i in range(signal.size):
            self.x2 = self.x1
            self.x1 = self.x0
            self.x0 = signal[i]
            self.y2 = self.y1
            self.y1 = self.y0
            self.y0 = self.K*(self.b0*self.x0 + self.b1*self.x1 + self.b2*self.x2 - self.a1*self.y1 - self.a2*self.y2)
            output[i] = self.y0
        return output
