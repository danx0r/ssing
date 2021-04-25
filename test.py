import os, sys, time, math
# import numpy as np
from scipy.io import wavfile as wf
import matplotlib.pyplot as plt
pi2 = math.pi*2

sr=40
sec=1
chunks=3
freq=3.4

# wo = np.zeros(sr*sec, np.int16)
wo = []
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

plt.plot(wo)
plt.show()