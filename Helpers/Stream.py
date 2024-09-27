import pyaudio
import numpy as np

class Stream:

    def __init__(self, stream_format=pyaudio.paFloat32, channels=1, is_input=True, frames_per_buffer=1024, sample_rate=44100):
        self.stream = None
        self.format = stream_format
        self.channels = channels
        self.input = is_input
        self.frame_per_buffer=frames_per_buffer
        self.stream = pyaudio.PyAudio().open(format=self.format, channels = self.channels, input=self.input, frames_per_buffer=self.frame_per_buffer, rate=sample_rate)

    def get_signal_segment(self, buffer_size=1024):
        buffer = self.stream.read(buffer_size)

        return np.fromstring(buffer, dtype=np.float32, sep='')