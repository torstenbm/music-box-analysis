import librosa

samples, sample_rate = librosa.load("music_box1.wav")

print(samples)
print(sample_rate)



import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt

sample_rate2, samples2 = wavfile.read("music_box1.wav")

print(samples2)
print(sample_rate2)

fft1 = abs(scipy.fft(samples))
fft2 = abs(scipy.fft(samples2))

frequencies = fftpk.fftfreq(len(fft2), (1.0/sample_rate2))

plt.plot(frequencies[range(len(fft2)//2)], fft2[range(len(fft2)//2)])
plt.xlabel("Frequency  (Hz)")
plt.ylabel("Amplitude")
plt.show()