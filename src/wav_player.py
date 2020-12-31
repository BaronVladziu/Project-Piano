# -*- coding: utf-8 -*-

import scipy.io.wavfile
import sounddevice as sd

class WavPlayer:
    def __init__(self, sampling_freq:int):
        self.sampling_freq = sampling_freq

    def play_signal(self, signal:"numpy.array"):
        sd.play(signal, self.sampling_freq)
        sd.wait()
        
    def save_signal(self, signal:"numpy.array"):
        scipy.io.wavfile.write("saved.wav", self.sampling_freq, signal)
