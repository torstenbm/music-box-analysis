import librosa
import librosa.display as display
import numpy as np
from matplotlib import pyplot as plt


# def plot_matrix(matrix, output_image_path=None, vmin=None, vmax=None, title=None):
#     """
#     Plot a 2D matrix with viridis color map
#
#     :param matrix: 2D numpy array
#     :return:
#     """
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     if title is not None:
#         ax.set_title(title)
#     plt.imshow(matrix, vmin=vmin, vmax=vmax)
#     plt.colorbar()
#     if output_image_path:
#         plt.savefig(str(output_image_path), dpi=200)
#     else:
#         plt.show()
#     plt.close(fig)

samples, sample_rate = librosa.load("music_box1.wav", sr=None)

fourier_output_stuff = np.abs(librosa.stft(samples, n_fft=16*1024))

frequencies = librosa.fft_frequencies(sr=sample_rate, n_fft=16*1024)
fourier_output_stuff = np.mean(fourier_output_stuff, axis=1)

plt.plot(frequencies, fourier_output_stuff)
plt.show()



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