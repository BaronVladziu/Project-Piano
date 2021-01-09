# -*- coding: utf-8 -*-

import numpy as np

from key_synthesizer import KeySynthesizer
from tools import midi2freq

class Synthesizer:
    def __init__(self, sampling_freq:int):
        self.sampling_freq = sampling_freq
        self.key_synthesizers = dict()
        for midi_nr in range(0, 128):
            self.key_synthesizers[midi_nr] = KeySynthesizer(sampling_freq, midi2freq(midi_nr))

    def pass_midi_signal(self, midi_nr:int, key_on:bool):
        if key_on:
            self.key_synthesizers[midi_nr].start()
        else:
            self.key_synthesizers[midi_nr].stop()

    def get_chunk(self, chunk_size:int) -> np.array:
        output = np.zeros(chunk_size)
        for key in self.key_synthesizers:
            output += self.key_synthesizers[key].get_chunk(chunk_size)
        return output
