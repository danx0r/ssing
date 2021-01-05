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
    # if i > len(wav)//2:
    for j in range(WINDOW//16, WINDOW-1):
        dft[j] = 0
    out.append( np.int16(np.real(np.fft.ifft(dft))) )
    i += WINDOW

wo = np.concatenate(out)

print (len(wo))
wf.write("out.wav", sr, wo)
