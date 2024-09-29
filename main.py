from Components.NoteRepeat import NoteRepeat
from Components.NotesCompare import NotesCompare
from Components.PitchDetector import PitchDetector

print("Choose components:")
print("1) Pitch Detector")
print("2) Note Repeat")
print("3) Note Compare")

item = input()

if item == '1':
    pitch_detector = PitchDetector()
    pitch_detector.start()
elif item == '2':
    note_repeat = NoteRepeat()
    note_repeat.start()
elif item == '3':
    notes_compare = NotesCompare()
    notes_compare.start()