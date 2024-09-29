from Constants.SharedValueConstants import semitone_map

class NoteHelper:

    @staticmethod
    def get_name_and_octave(note):
        # Extract the note name and octave
        if len(note) == 2:  # e.g., C4
            note_name = note[0]
            octave = int(note[1])
        elif len(note) == 3:  # e.g., C#5 or A#4
            note_name = note[:2]
            octave = int(note[2])
        else:
            raise ValueError("Invalid note format")

        return note_name, octave

    @staticmethod
    def to_frequency(note):
        note_name, octave = NoteHelper.get_name_and_octave(note)

        # Calculate the number of half steps from A4
        half_steps = semitone_map[note_name] + (octave - 4) * 12

        # Calculate frequency
        frequency = 440.0 * (2 ** (half_steps / 12))

        return frequency

    @staticmethod
    def to_midi_number(note):
        note_name, octave = NoteHelper.get_name_and_octave(note)

        midi = 69 + (12 * (octave - 4)) + semitone_map[note_name]

        return midi