#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from biquad import Biquad
# from pulse_generator import PulseGenerator
# from wav_player import WavPlayer

# def main():
#     # Generate signal
#     pulse_generator = PulseGenerator(sampling_freq=44100)
#     signal = pulse_generator.generate(freq=200, length=1)
#     biquad = Biquad()
#     biquad.randomize_params()
#     signal = biquad.filter(signal)

#     # Save signal
#     wav_player = WavPlayer(sampling_freq=44100)
#     wav_player.save_signal(signal)
#     wav_player.play_signal(signal)

# if __name__ == "__main__":
#     main()



import rtmidi
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

from synthesizer import Synthesizer
from tools import midi2freq


midiin = rtmidi.RtMidiIn()

def print_message(midi):
    if midi.isNoteOn():
        print('ON: ', midi.getNoteNumber(), midi2freq(midi.getNoteNumber()), midi.getVelocity())
    elif midi.isNoteOff():
        print('OFF:', midi.getNoteNumber(), midi2freq(midi.getNoteNumber()), midi.getVelocity())
    elif midi.isController():
        print('CONTROLLER', midi.getControllerNumber(), midi.getControllerValue())


ports = range(midiin.getPortCount())
if ports:
    for i in ports:
        print("Port", i, ':', midiin.getPortName(i))
    midiin.openPort(1)

    fs = 44100  # sampling rate, Hz, must be integer
    chunk = 128  # in samples
    volume = 0.1

    synthesizer = Synthesizer(fs)
    stream = sd.OutputStream(fs, chunk, channels=1)

    with stream:
        nr_synthesized_chunks = 0
        buf_size_in_chunks = 10000
        bufor = np.zeros(buf_size_in_chunks * chunk)

        # frame_nr = 0
        while True:
            m = midiin.getMessage(1)  # some timeout in ms
            if m:
                print_message(m)
                if m.isNoteOn():
                    synthesizer.pass_midi_signal(
                        midi_nr=m.getNoteNumber(),
                        key_on=True
                    )
                else:
                    synthesizer.pass_midi_signal(
                        midi_nr=m.getNoteNumber(),
                        key_on=False
                    )

            # generate samples, note conversion to float32 array
            samples = synthesizer.get_chunk(chunk).astype(np.float32)
            stream.write(volume * samples)

else:
    print('NO MIDI INPUT PORTS!')