import os, sys, time, math
# import numpy as np
from scipy.io import wavfile as wf
import matplotlib.pyplot as plt

sr=40
sec=1
chunks=2
freq=3

# wo = np.zeros(sr*sec, np.int16)
wo = []
for chunk in range(chunks):
    for i in range(sr*sec):
        # s = i % 256 * 16
        t = i/sr
        s = math.sin(t*freq*math.pi*2)
        wo.append(s)

    # wf.write("out.wav", sr, wo)

# print(wo)

plt.plot(wo)
plt.show()