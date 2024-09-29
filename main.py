from Components.NoteImitation import NoteImitation
from Components.PitchDetector import PitchDetector

print("Choose components:")
print("1) Pitch Detector")
print("2) Note Imitation")

item = input()

if item == '1':
    pitchDetector = PitchDetector()
    pitchDetector.start()
elif item == '2':
    noteImitation = NoteImitation()
    noteImitation.start()