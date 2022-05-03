import sounddevice as sd
from scipy.io.wavfile import write
from google_trans_new import google_translator
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import wavio as wv
from os import path
fs = 44100
seconds = 3
myrecording = sd.rec(int(seconds*fs),samplerate=fs,channels=2)
sd.wait()

wv.write('output.mp3', myrecording, fs, sampwidth=seconds)
r=sr.Recognizer()
file=sr.AudioFile('output.mp3')
with file as source:
    r.adjust_for_ambient_noise(source)
    audio=r.record(source, duration=10)
    result=r.recognize_google(audio,language='en')
translator = google_translator()
translation = translator.translate(result,lang_src="en",lang_tgt="mr")
myobj = gTTS(text=translation, lang="mr", slow=False) 
myobj.save(path.expandvars(r"%AppData%\Translation.mp3"))
playsound(path.expandvars(r"%AppData%\Translation.mp3"))
os.remove(path.expandvars(r"%AppData%\Translation.mp3"))