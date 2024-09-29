import os
import time

import aubio
import random
import threading
import subprocess

from Helpers.NoteHelper import NoteHelper
from Infrastructure.Streamer import Streamer
from Infrastructure.MidiPlayer import MidiPlayer
from Helpers.MidiHelper import MidiHelper

class NoteHearAndSing:

    def __init__(self):
        self.midi_player = MidiPlayer()
        self.stream = Streamer()

        self.pitch_o = aubio.pitch("default", 4096, 1024)
        self.pitch_o.set_unit("midi")

        self.print_lock = threading.Lock()

        self.current_midi = None
        self.done = False

    def start(self):
        os.system("clear")

        thread1 = threading.Thread(target=self.play_random_notes)
        thread2 = threading.Thread(target=self.show_audio)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        os.system("clear")

    def play_random_notes(self, low_note='C3', high_note='C5'):
        low_midi_number, high_midi_number = NoteHelper.to_midi_number(low_note), NoteHelper.to_midi_number(high_note)

        self.current_midi, n = random.randint(low_midi_number, high_midi_number + 1), 1

        while True:
            note = MidiHelper.to_note_with_octave(self.current_midi)
            print("Note Hear and Sing Practice.")
            print("Press r to repeat, q to quit, and Enter to the next question!")
            print(f"Question {n}")
            print(f"Playing: {note}\n")
            self.midi_player.play_midi_number(self.current_midi)
            key = input()
            subprocess.call('clear', shell=True)
            with self.print_lock:
                if key == 'r':
                    continue
                elif key == 'q':
                    self.done = True
                    print("Goodbye!")
                    time.sleep(1)
                    break
                else:
                    n += 1
                    self.current_midi = random.randint(low_midi_number, high_midi_number + 1)

    def show_audio(self):
        while True:
            signal = self.stream.get_signal_segment()
            midi_number = int(round(self.pitch_o(signal)[0]))
            try:
                note = MidiHelper.to_note_with_octave(midi_number)
            except ValueError as e:
                continue

            feedback = "high" if midi_number > self.current_midi else "low" if midi_number < self.current_midi else "correct"
            if self.print_lock.locked():
                continue
            elif self.done:
                break
            else:
                print(f"\033[FSinging: {note} {feedback}", end="    \n")