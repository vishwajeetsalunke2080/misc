# Importing necessary modules required 
import speech_recognition as sr 
from google_trans_new import google_translator 
from gtts import gTTS 
import os 
from scipy.io.wavfile import write 
import wavio as wv 
import sounddevice as sd

# Creating Recogniser() class object 
 

	

translator = google_translator()
from_lang = input("source language")
to_lang = input("destination language")
freq = 44100
duration = 10
recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=2) 
sd.wait(200) 
wv.write(r"C:\AppData\assistantdata.wav", recording, freq, sampwidth=1)
r = sr.Recognizer()
file=sr.AudioFile(r'C:\AppData\assistantdata.wav')
with file as source:
	r.adjust_for_ambient_noise(source)
	audio=r.record(source, duration=10)
	result=r.recognize_google(audio,language='en') 
print("Phase to be Translated :"+ result) 
translation = translator.translate(result,lang_src=from_lang,lang_tgt=to_lang)
text = translation
speak = gTTS(text=text, lang=to_lang, slow= False) 
speak.save("captured_voice.mp3")	 
os.system("start captured_voice.mp3") 
