import os, sys, time
import numpy as np
from scipy.io import wavfile as wf

WINDOW = 44100 // 25

fn = sys.argv[1]

sr, wav =  wf.read(fn)

i = 0
out = []
while i < len(wav)-WINDOW:
    dft = np.fft.fft(wav[i: i+WINDOW])

    for j in range(WINDOW):
        if j >= WINDOW//2:
            dft[j] = 0               #rm neg half, vol X 2 to compensate
        else:
            dft[j] *= 2

        #zero out phase
        dft[j] = np.complex(np.absolute(dft[j]), 0)

    idft = np.fft.ifft(dft)
    ireal = np.real(idft)

    out.append(np.int16(ireal))
    i += WINDOW

wo = np.concatenate(out)

print (len(wo))
wf.write("out.wav", sr, wo)
