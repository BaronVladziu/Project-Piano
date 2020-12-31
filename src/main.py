#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pulse_generator import PulseGenerator
from wav_player import WavPlayer

def main():
    # Generate signal
    pulse_generator = PulseGenerator(sampling_freq=44100)
    signal = pulse_generator.generate(freq=500, length=1)

    # Save signal
    wav_player = WavPlayer(sampling_freq=44100)
    wav_player.save_signal(signal)
    wav_player.play_signal(signal)

if __name__ == "__main__":
    main()
