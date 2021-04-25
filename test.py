import os, sys, time, math
import numpy as np
from scipy.io import wavfile as wf
import matplotlib.pyplot as plt
pi2 = math.pi*2

sr=40
sec=1
chunks=3
freq=3.4

def plot_complex(a):
    mag = []
    phase = []
    for x in a:
        mag.append(abs(x))
        p = np.angle(x) % pi2
        phase.append(p)
    plt.plot(mag)
    plt.plot(phase)

# wo = np.zeros(sr*sec, np.int16)
wo = []
dfts=[]
phase = 0
for chunk in range(chunks):
    for i in range(sr*sec):
        t = i/sr
        yy = phase + t * freq * pi2
        s = math.sin(yy)
        wo.append(s)
    i += 1
    t = i / sr
    phase = (phase + t * freq * pi2) % pi2
    print (phase)
    j = len(wo)
    dft = np.fft.fft(wo[j-sr: j])
    dfts.append(dft)

plt.plot(wo)
plt.show()
for dft in dfts:
    plot_complex(dft)
    plt.show()
