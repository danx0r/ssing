import os, sys, time, math
import numpy as np
from scipy.io import wavfile as wf

sr=44100
sec=3

wo = np.zeros(sr*sec, np.int16)

for i in range(sr*sec):
    # s = i % 256 * 16
    t = i/sr
    f = 440
    s = math.sin(t*f*math.pi*2) * 10000
    wo[i] = s

wf.write("out.wav", sr, wo)
