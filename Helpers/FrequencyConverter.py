import numpy as np

from Constants.PitchFrequency import PitchFrequency
from Enums.Note import Note

class FrequencyConverter:

    ref_frequency = PitchFrequency.A4
    note_list = [Note.C, Note.CSharp, Note.D, Note.DSharp, Note.E, Note.F, Note.FSharp, Note.G, Note.GSharp, Note.A, Note.ASharp, Note.B]

    @staticmethod
    def get_note_name(frequency):
        if np.abs(frequency) < 1:
            return ""

        semitone_diff = 12 * np.log2(frequency / FrequencyConverter.ref_frequency)

        nearest_note = round(semitone_diff)

        note_index = (nearest_note + 9) % 12  # +9 to make A4 = 0 semitone distance
        octave = 4 + (nearest_note + 9) // 12  # Adjust octave for A4 reference

        note_name = FrequencyConverter.note_list[note_index]

        return f"{note_name.value}{octave}"