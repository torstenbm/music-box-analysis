import librosa
from scipy.signal import find_peaks_cwt
import numpy as np
from matplotlib import pyplot as plt

notes = [
    "music_box1.wav",
    "music_box2.wav",
    "music_box3.wav",
    "music_box4.wav",
    "music_box5.wav",
    "music_box6.wav",
]

for note in notes:
    samples, sample_rate = librosa.load(note, sr=None)

    spectrogram = np.abs(librosa.stft(samples, n_fft=16 * 1024))

    frequencies = librosa.fft_frequencies(sr=sample_rate, n_fft=16*1024)
    spectrogram = np.mean(spectrogram, axis=1)

    dominant_harmonic_index = np.where(spectrogram == np.max(spectrogram))
    print(frequencies[dominant_harmonic_index])

    # peaks = find_peaks_cwt(fourier_output_stuff, widths=np.ones(1000)) Tried finding more peaks with this, but little luck

    plt.plot(frequencies, spectrogram)
    plt.xscale("log")
    plt.yscale("log")
    # plt.plot(peaks, fourier_output_stuff[peaks], "x")
    plt.title(note)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.show()