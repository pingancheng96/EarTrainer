import matplotlib.pyplot as plt
import aubio

from Helpers.MidiHelper import MidiHelper
from Helpers.StreamHelper import Stream
from collections import deque

class Detector:
    REFRESH_RATE_IN_SECONDS = 0.00001
    FRAMES_TO_DISPLAY = 10

    MIN_MIDI, MAX_MIDI = 60, 80
    MIDI_RANGE = range(MIN_MIDI, MAX_MIDI)
    NOTE_RANGE = [MidiHelper.convert_to_note(x) for x in MIDI_RANGE]

    def __init__(self):
        self.stream = Stream()
        self.pitch_o = aubio.pitch("default", 4096, 1024)
        self.pitch_o.set_unit("midi")

    def start(self):
        time_segment = 0

        time_series = deque()
        frequency_series = deque()
        note_series = deque()

        plt.ion()

        while True:
            try:
                signal = self.stream.get_signal_segment()
                midi = int(round(self.pitch_o(signal)[0]))
                note = "" if MidiHelper.is_invalid_midi_number(midi) else MidiHelper.convert_to_note(midi)

                time_series.append(time_segment)
                frequency_series.append(midi)
                note_series.append(note)

                plt.yticks(Detector.MIDI_RANGE, Detector.NOTE_RANGE)
                plt.ylim(Detector.MIN_MIDI, Detector.MAX_MIDI)

                plt.plot(time_series, frequency_series)
                plt.draw()
                plt.pause(Detector.REFRESH_RATE_IN_SECONDS)
                plt.clf()

                time_segment += 1

                if len(time_series) > Detector.FRAMES_TO_DISPLAY:
                    time_series.popleft()
                    frequency_series.popleft()
                    note_series.popleft()

            except KeyboardInterrupt:
                print("*** Ctrl+C pressed, exiting")
                break

detector = Detector()
detector.start()