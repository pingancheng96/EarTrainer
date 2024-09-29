import os
import aubio
import matplotlib.pyplot as plt
from Helpers.MidiHelper import MidiHelper
from Infrastructure.Streamer import Streamer
from collections import deque

class FreeSinging:
    REFRESH_RATE_IN_SECONDS = 0.000001
    FRAMES_TO_DISPLAY = 10

    MIN_MIDI, MAX_MIDI = 60, 80
    MIDI_RANGE = range(MIN_MIDI, MAX_MIDI)
    NOTE_RANGE = [MidiHelper.to_note_with_octave(x) for x in MIDI_RANGE]

    def __init__(self):
        self.stream = Streamer(sample_rate=12800)
        self.pitch_o = aubio.pitch("default", 4096, 1024)
        self.pitch_o.set_unit("midi")

    def start(self):
        os.system("clear")
        time_segment = 0

        time_series = deque()
        frequency_series = deque()
        note_series = deque()

        plt.ion()

        print("Pitch detecting...")

        while True:
            try:
                signal = self.stream.get_signal_segment()
                midi = int(round(self.pitch_o(signal)[0]))
                note = "" if MidiHelper.is_invalid_midi_number(midi) else MidiHelper.to_note_with_octave(midi)

                time_series.append(time_segment)
                frequency_series.append(midi)
                note_series.append(note)

                plt.yticks(FreeSinging.MIDI_RANGE, FreeSinging.NOTE_RANGE)
                plt.ylim(FreeSinging.MIN_MIDI, FreeSinging.MAX_MIDI)

                plt.plot(time_series, frequency_series)
                plt.draw()
                plt.pause(FreeSinging.REFRESH_RATE_IN_SECONDS)
                plt.clf()

                time_segment += 1

                if len(time_series) > FreeSinging.FRAMES_TO_DISPLAY:
                    time_series.popleft()
                    frequency_series.popleft()
                    note_series.popleft()

            except KeyboardInterrupt:
                print("*** Ctrl+C pressed, exiting")
                break