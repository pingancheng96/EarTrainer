import os
import time
import numpy as np

from Helpers.NoteHelper import NoteHelper
from Infrastructure.MidiPlayer import MidiPlayer

class NotesCompare:

    def __init__(self):
        self.midi_player = MidiPlayer()

    def start(self,low_note='C3',high_note='C5'):

        low_midi, high_midi = NoteHelper.to_midi_number(low_note), NoteHelper.to_midi_number(high_note)

        first, second = NotesCompare.get_two_different_notes_in_range(low_midi, high_midi)
        prev_first, prev_second = first, second

        total, correct, prev_result = 0, 0, True

        while True:
            os.system("clear")
            print(f"Question {total}: which note is higher? Press 1 or 2.\nPress q to quit, r to repeat current question, p to retry previous question.")

            self.midi_player.play_midi_number(first,duration=1)
            self.midi_player.play_midi_number(second, duration=1)

            truth = 1 if first > second else 2

            answer = input()

            if answer == '1' or answer == '2':
                if int(answer) == truth:
                    correct, prev_result = correct + 1, prev_result
                    print("correct")
                else:
                    prev_result = False
                    print("incorrect")
                total += 1
            if answer == 'q':
                break
            if answer == 'r':
                continue
            if answer == 'p':
                first, second = prev_first, prev_second
                total, correct = total - 1, correct - 1 if prev_result == True else correct
                continue

            prev_first, prev_second = first, second
            first, second = NotesCompare.get_two_different_notes_in_range(low_midi, high_midi)

            time.sleep(1)

        print(f"{correct} out of {total} is correct. accuracy: {correct/total}\nGoodbye!")

    @staticmethod
    def get_two_different_notes_in_range(low, high):
        first, second = None, None

        while first == second:
            first, second = np.random.randint(low, high + 1), np.random.randint(low, high + 1)

        return first, second