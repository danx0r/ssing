import sys
from librosa import griffinlim
from librosa.feature import melspectrogram as mel
from librosa.feature.inverse import mel_to_audio as imel
from librosa.feature.inverse import mel_to_stft as m2stft
from librosa import load
import soundfile as sf
import numpy as np

MELS=188
SR=44100
HOP=256
FFT=1024

def rmse(a, b):
    return sum(sum((a-b)**2))**.5

aud=load(sys.argv[1], SR)[0]
m=mel(aud,sr=44100, hop_length=HOP, n_fft=FFT, n_mels=MELS)
if len(sys.argv) > 2:
    aud=load(sys.argv[2], sr=SR)[0]
    m2 = mel(aud, sr=SR, hop_length=HOP, n_fft=FFT, n_mels=MELS)
    dif = rmse(m, m2)
    print ("err:", dif)
else:
    rec=imel(m, sr=SR, hop_length=HOP, n_fft=FFT)
    # S = m2stft(m, sr=44100, n_fft=1024)
    # rec = griffinlim(S, hop_length=256)
    sf.write('mel_recon.wav', rec, SR)

    # for y in m:
    #     row = ""
    #     for x in y:
    #         row += f"{x}, "
    #     print (row)
