import os
import time

import numpy as np

from Helpers.MidiHelper import MidiHelper
from Helpers.NoteHelper import NoteHelper
from Infrastructure.MidiPlayer import MidiPlayer

class MelodyTrend:

    def __init__(self):
        self.midi_player = MidiPlayer()

    def start(self,low_note='C3',high_note='C5', num_notes=3):

        low_midi, high_midi = NoteHelper.to_midi_number(low_note), NoteHelper.to_midi_number(high_note)

        notes = [MidiHelper.get_midi_in_range(low_midi, high_midi) for x in range(num_notes)]
        prev_notes = [x for x in notes]

        total, correct, prev_result = 0, 0, True

        while True:
            os.system("clear")
            print("Melody Trend Practice")
            print("Press q to quit, r to repeat current question, p to retry previous question.")
            print("Give the pitch trend of a melody. u for up, d for down, e for equal.")
            print("For example, if you hear C4 D3 E4 F#4, you should type duu.")
            print(f"Question {total}:")

            for note in notes:
                self.midi_player.play_midi_number(note,duration=1)

            truth = ''.join([MelodyTrend.compare_notes(notes[i - 1], notes[i]) for i in range(1, len(notes))])

            answer = input()

            if answer == 'q':
                break
            if answer == 'r':
                continue
            if answer == 'p':
                notes = [prev_note for prev_note in prev_notes]
                total, correct = total - 1, correct - 1 if prev_result == True else correct
                time.sleep(1)
                continue
            if answer == truth:
                correct, prev_result = correct + 1, prev_result
                print("correct")
            else:
                prev_result = False
                print("incorrect")
            total += 1

            prev_notes = [note for note in notes]
            notes = [MidiHelper.get_midi_in_range(low_midi, high_midi) for x in range(num_notes)]

            time.sleep(1)

        print(f"{correct} out of {total} is correct. accuracy: {correct/total}\nGoodbye!")

    @staticmethod
    def get_two_different_notes_in_range(low, high):
        first, second = None, None

        while first == second:
            first, second = np.random.randint(low, high + 1), np.random.randint(low, high + 1)

        return first, second

    @staticmethod
    def compare_notes(note1, note2):
        if note1 == note2:
            return 'e'
        if note1 > note2:
            return 'd'
        if note1 < note2:
            return 'u'