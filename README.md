# Exercise 2 - Analyze the music box as a sound source


## Make a recording of the sound from the music box as you hold it in the hand

The result file is called `music_box.wav`.

## Cut up the recording into individual tones
This was accomplished using Audacity, the notes are labeled `music_boxN.wav` with `1<=N<=6`.


## Analyze the spectra for each individual tone
### Take an fft of each individual tone and identify a number of peaks.

This was done using the librosa library and a big fft-window size to easier discover peaks,
the results have been plotted for each note and stored in their respective png-files.
The frequencies of the peaks were printed to the console as

441.43066406

331.07299805

293.38989258

331.07299805

349.91455078

524.87182617

### Show which of the tones are harmonically related.
I was not able to find any integer relationship between the fundamental frequencies of
the notes, and must therefore conclude that none of them where harmonically related.

###  How many harmonic components can you identify?
When plotting linearly I could only identify the fundamentals, however, when plotting
with log-scale I could see about 6-8 harmonics for each note.

###  What are their relative levels?
They differed from the fundamental by a factor of about `10**2` (100 times smaller).

###  Express the levels in dB.
I tried calculating using `d = log(a/a0)`, but got 160db which must be wrong (`a = 10**3, a0 = 10**-5`).
I guess I am not sure what the y-axis of my stft represents, and would love feedback on this.

### What is the uncertainty in your frequency estimates?


## What musical notes are played?
According to https://pages.mtu.edu/~suits/notefreqs.html the musical notes are

441.43066406 A

331.07299805 E

293.38989258 D

331.07299805 E

349.91455078 F

524.87182617 C