import fluidsynth
import time

class MidiPlayer:
    def __init__(self):
        self.sf = fluidsynth.Synth()
        self.sf.start(driver="coreaudio")
        self.soundfont_id = self.sf.sfload("SoundFont/alex_gm.sf2")
        self.sf.program_select(0, self.soundfont_id, 0, 0)

    def play_midi_number(self, midi, duration=1, velocity=100):

        self.sf.noteon(0, midi, velocity)  # Start playing note (channel 0, velocity 100)
        time.sleep(duration)  # Play for the specified duration
        self.sf.noteoff(0, midi)
