from librosa.feature import melspectrogram as mel
from librosa.feature.inverse import mel_to_audio as imel
from librosa import load
import soundfile as sf

aud=load("old/mel4.wav", sr=44100)[0]
m=mel(aud,sr=44100, hop_length=256, n_fft=1024)
rec=imel(m, sr=44100, hop_length=256, n_fft=1024)
sf.write('mel_recon.wav', rec, 44100)
