import librosa
import numpy as np

class AudioAnalyzer:

    def __init__(self):
        self.frequencies_index_ratio = 0
        self.time_index_ratio = 0
        self.spectrogram = None

    def load(self, filename):
        time_series, sample_rate = librosa.load(filename)
        stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048 * 4))
        self.spectrogram = librosa.amplitude_to_db(stft, ref=np.max)
        frequencies = librosa.core.fft_frequencies(n_fft=2048 * 4)
        times = librosa.core.frames_to_time(np.arange(self.spectrogram.shape[1]), sr=sample_rate, hop_length=512, n_fft=2048 * 4)
        self.time_index_ratio = len(times) / times[-1]
        self.frequencies_index_ratio = len(frequencies) / frequencies[-1]

    def get_decibel(self, target_time, freq):
        return self.spectrogram[int(freq * self.frequencies_index_ratio)][int(target_time * self.time_index_ratio)]
