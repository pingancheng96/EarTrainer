import aubio

class FrequencyParser:

    pitch_o = aubio.pitch("default", 4096, 1024)

    @staticmethod
    def get_frequency(signal):
        return FrequencyParser.pitch_o(signal)[0]
