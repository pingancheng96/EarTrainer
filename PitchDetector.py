from Helpers.FrequencyConverter import FrequencyConverter
from Helpers.FrequencyParser import FrequencyParser
from Helpers.Stream import Stream

class Detector:

    def __init__(self):
        self.stream = Stream()

    def start(self):

        while True:
            try:
                signal = self.stream.get_signal_segment()
                frequency = FrequencyParser.get_frequency(signal)
                note = FrequencyConverter.get_note_name(frequency)

                print(f"{note}")

            except KeyboardInterrupt:
                print("*** Ctrl+C pressed, exiting")
                break

detector = Detector()
detector.start()