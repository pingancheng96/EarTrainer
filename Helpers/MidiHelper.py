import numpy as np
from Constants.SharedValueConstants import *

class MidiHelper:
    @staticmethod
    def to_note_with_octave(midi):
        if MidiHelper.is_invalid_midi_number(midi):
            raise ValueError("invalid midi number")

        note_index = midi % 12
        octave = (midi // 12) - 1  # Calculate octave (MIDI note 0 is C-1)
        note = semitones[note_index]  # Find the note name (C, C#, D, etc.)

        return f"{note}{octave}"

    @staticmethod
    def is_invalid_midi_number(midi):
        return midi is None or midi < midi_min or midi > midi_max

    @staticmethod
    def get_midi_in_range(low, high):
        return np.random.randint(low, high + 1)