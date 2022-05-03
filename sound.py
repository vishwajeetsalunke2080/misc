import sounddevice as sd 
from scipy.io.wavfile import write 
import wavio as wv 
import speech_recognition as sr
import pyttsx3
import os
import subprocess
import logging
from tkinter import *
from PIL import ImageTk,Image
import tkinter
from tkinter import Button
from tkinter import Tk

root=Tk()
root.geometry('500x500')
root.title("Danny Assistant")

freq = 44100
duration = 10
recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=2) 


sd.wait(10) 
wv.write("welcome1.wav", recording, freq, sampwidth=1)
r=sr.Recognizer()
file=sr.AudioFile('welcome1.wav')
with file as source:
    r.adjust_for_ambient_noise(source)
    audio=r.record(source, duration=22)
	

result=r.recognize_google(audio,language='en')
print(result)

engine=pyttsx3.Engine()
said="user said"+result
engine.say(said)
engine.runAndWait()	

user_speech=[]
for i in range(10000):
	user_speech.append(result)

result=result.lower()
note='open notepad'
if note in result:
	os.system('cmd /c notepad.exe')
command='open control panel'
if command in result:
	os.system('cmd /c control.exe')
command='play music'
if command in result:
	os.system('cmd /c "G:\Tu Jaane Na - Atif Aslam - 320Kbps.mp3"')

command='open chrome'
if command in result:
	os.system('cmd /c start chrome.exe')



root.mainloop()
