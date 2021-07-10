import sys
from librosa import griffinlim
from librosa.feature import melspectrogram as mel
from librosa.feature.inverse import mel_to_audio as imel
from librosa.feature.inverse import mel_to_stft as m2stft
from librosa import load
import soundfile as sf
import numpy as np

MELS=100
SR=44100
HOP=256
FFT=1024

def rmse(a, b):
    return sum(sum((a-b)**2))**.5

def wav2freq(filename):
    audio =load(filename, SR)[0]
    freq_data = mel(audio,sr=44100, hop_length=HOP, n_fft=FFT, n_mels=MELS)
    return freq_data
    
def write_wav(freq_data, outfile='mel_recon.wav'):
    rec=imel(freq_data, sr=SR, hop_length=HOP, n_fft=FFT)
    sf.write(outfile, rec, SR)
    return