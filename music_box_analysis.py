import librosa
import librosa.display as display
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

    fourier_output_stuff = np.abs(librosa.stft(samples, n_fft=16*1024))

    frequencies = librosa.fft_frequencies(sr=sample_rate, n_fft=16*1024)
    fourier_output_stuff = np.mean(fourier_output_stuff, axis=1)

    dominant_harmonic_index = np.where(fourier_output_stuff == np.max(fourier_output_stuff))
    print(frequencies[dominant_harmonic_index])

    plt.plot(frequencies, fourier_output_stuff, note)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.show()

# https://pages.mtu.edu/~suits/notefreqs.html


# db = librosa.amplitude_to_db(fourier_output_stuff, ref=np.max)
# display.specshow(db, sr=sample_rate, y_axis='log', x_axis='time')









































#
# print(samples)
# print(sample_rate)
#
#
#
# import scipy.io.wavfile as wavfile
# import scipy
# import scipy.fftpack as fftpk
# import numpy as np
#
# sample_rate2, samples2 = wavfile.read("music_box1.wav")
#
# print(samples2)
# print(sample_rate2)
#
# fft1 = abs(scipy.fft(samples))
# fft2 = abs(scipy.fft(samples2))
#
# frequencies = fftpk.fftfreq(len(fft2), (1.0/sample_rate2))
#
# plt.plot(frequencies[range(len(fft2)//2)], fft2[range(len(fft2)//2)])
# plt.xlabel("Frequency  (Hz)")
# plt.ylabel("Amplitude")
# plt.show()