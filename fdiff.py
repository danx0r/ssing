import os, sys, time
import numpy as np
from scipy.io import wavfile as wf

WINDOW = 44100 // 25

fn1 = sys.argv[1]
fn2 = sys.argv[2]

sr, w1 =  wf.read(fn1)
sr, w2 =  wf.read(fn2)

i = 0
tot = min(len(w1), len(w2))
cnt = tot // WINDOW
errs = []
while i < tot - WINDOW:
    d1 = np.fft.fft(w1[i: i + WINDOW])
    d1 = np.absolute(d1)
    d2 = np.fft.fft(w2[i: i + WINDOW])
    d2 = np.absolute(d2)
    d = d1-d2
    d2 = d * d
    avg = np.average(d2)
    rmse = avg ** .5
    errs.append(rmse)
    i += WINDOW

err = sum(errs) / len(errs)

print ("ERR:", err)