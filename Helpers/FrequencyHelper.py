import numpy as np

from Constants.SharedValueConstants import semitones
from Constants.SharedValueConstants import A4_frequency

class FrequencyHelper:

    @staticmethod
    def convert_frequency_to_note(frequency):
        if np.abs(frequency) < 1:
            return ""

        semitone_diff = 12 * np.log2(frequency / A4_frequency)

        nearest_note = round(semitone_diff)

        note_index = (nearest_note + 9) % 12  # +9 to make A4 = 0 semitone distance
        octave = 4 + (nearest_note + 9) // 12  # Adjust octave for A4 reference

        note = semitones[note_index]

        return f"{note.Name}{octave}"

    @staticmethod
    def to_midi_number(frequency):
        midi = 69 + 12 * np.log2(frequency / A4_frequency)
        return round(midi)