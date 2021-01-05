import os, sys, time
import numpy as np
from scipy.io import wavfile as wf

WINDOW = 44100 // 25

fn1 = sys.argv[1]
fn2 = sys.argv[2]

sr, w1 =  wf.read(fn1)
sr, w2 =  wf.read(fn2)

i = 0
out = []
while i < len(wav)-WINDOW:
    dft = np.fft.fft(wav[i: i+WINDOW])
    if i > len(wav)//2:
        for j in range(WINDOW//32, WINDOW-WINDOW//32-1):
            dft[j] = 0
    out.append( np.int16(np.real(np.fft.ifft(dft))) )
    i += WINDOW

wo = np.concatenate(out)

print (len(wo))
wf.write("out.wav", sr, wo)
