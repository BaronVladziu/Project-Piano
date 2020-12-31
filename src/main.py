#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from biquad import Biquad
from pulse_generator import PulseGenerator
from wav_player import WavPlayer

def main():
    # Generate signal
    pulse_generator = PulseGenerator(sampling_freq=44100)
    signal = pulse_generator.generate(freq=200, length=1)
    biquad = Biquad()
    biquad.randomize_params()
    signal = biquad.filter(signal)

    # Save signal
    wav_player = WavPlayer(sampling_freq=44100)
    wav_player.save_signal(signal)
    wav_player.play_signal(signal)

if __name__ == "__main__":
    main()
