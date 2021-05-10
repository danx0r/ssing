import sys
from librosa import griffinlim
from librosa.feature import melspectrogram as mel
from librosa.feature.inverse import mel_to_audio as imel
from librosa.feature.inverse import mel_to_stft as m2stft
from librosa import load
import soundfile as sf

aud=load(sys.argv[1], sr=44100)[0]
m=mel(aud,sr=44100, hop_length=256, n_fft=1024)
# rec=imel(m, sr=44100, hop_length=256, n_fft=1024)
S = m2stft(m, sr=44100, n_fft=1024)
rec = griffinlim(S, hop_length=256)
sf.write('mel_recon.wav', rec, 44100)
