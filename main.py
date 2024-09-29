from Practice.NoteHearAndSing import NoteHearAndSing
from Practice.MelodyTrend import MelodyTrend
from Practice.FreeSinging import FreeSinging

print("Choose practice:")
print("1) Free Singing")
print("2) Note Hear and Sing")
print("3) Melody Trend")

item = input()

if item == '1':
    free_singing = FreeSinging()
    free_singing.start()
elif item == '2':
    note_hear_and_sing = NoteHearAndSing()
    note_hear_and_sing.start()
elif item == '3':
    num_notes = int(input("How many notes in a question?\n"))
    melody_trend_practice = MelodyTrend()
    melody_trend_practice.start(num_notes=num_notes)