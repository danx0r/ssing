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
base = []
while i < tot - WINDOW:
    d1 = np.fft.fft(w1[i: i + WINDOW//8])
    d1 = np.absolute(d1)
    d2 = np.fft.fft(w2[i: i + WINDOW//8])
    d2 = np.absolute(d2)
    d = d1-d2

    #calc baseline
    dsq = d1 * d1
    avg = np.average(dsq)
    rmse = avg ** .5
    base.append(rmse)

    #calc diff
    dsq = d * d
    avg = np.average(dsq)
    rmse = avg ** .5
    errs.append(rmse)

    i += WINDOW

base = sum(base) / len(base)
err = sum(errs) / len(errs)
similarity = base-err
dif = err/base

print ("ERR", err, "BASE", base, "SIM:", similarity, "DIF", dif)