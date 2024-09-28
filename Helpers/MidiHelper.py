from logging import exception


from Constants.Note import Note

from Constants.MidiNumber import MidiNumber

class MidiHelper:

    NOTE_LIST = [Note.C, Note.CSharp, Note.D, Note.DSharp, Note.E, Note.F, Note.FSharp, Note.G, Note.GSharp, Note.A, Note.ASharp, Note.B]

    @staticmethod
    def convert_to_note(midi_number):
        if MidiHelper.is_invalid_midi_number(midi_number):
            return exception("invalid midi number")

        octave = (midi_number // 12) - 1  # Calculate octave (MIDI note 0 is C-1)
        note = MidiHelper.NOTE_LIST[midi_number % 12]  # Find the note name (C, C#, D, etc.)

        return f"{note.Name}{octave}"

    @staticmethod
    def is_invalid_midi_number(midi_number):
        return midi_number is None or midi_number < MidiNumber.Min or midi_number > MidiNumber.Max