import numpy as np

from Constants.Note import Note

class FrequencyHelper:

    REF_FREQUENCY = Note.A.StandardFrequency
    NOTE_LIST = [Note.C, Note.CSharp, Note.D, Note.DSharp, Note.E, Note.F, Note.FSharp, Note.G, Note.GSharp, Note.A, Note.ASharp, Note.B]

    @staticmethod
    def convert_frequency_to_note(frequency):
        if np.abs(frequency) < 1:
            return ""

        semitone_diff = 12 * np.log2(frequency / FrequencyHelper.REF_FREQUENCY)

        nearest_note = round(semitone_diff)

        note_index = (nearest_note + 9) % 12  # +9 to make A4 = 0 semitone distance
        octave = 4 + (nearest_note + 9) // 12  # Adjust octave for A4 reference

        note = FrequencyHelper.NOTE_LIST[note_index]

        return f"{note.Name}{octave}"