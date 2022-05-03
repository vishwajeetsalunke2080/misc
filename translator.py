import speech_recognition as sr 
from translate import Translator 
from gtts import gTTS
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os 
from os import path


def translate():
        
        translator = Translator(from_lang="en", to_lang="mar")
        auto=text.get("1.0","end")
        translation = translator.translate(auto)
        t2.insert('1.0', translation)
        myobj = gTTS(text=translation, lang="mar", slow=False) 
        myobj.save("welcome.mp3") 
        os.system("welcome.mp3")
        

def speech_demo():
    r=sr.Recognizer()
    file=sr.AudioFile('demo.wav')
    with file as source:
        r.adjust_for_ambient_noise(source)
        audio=r.record(source, duration=5)
        result=r.recognize_google(audio,show_all=True,language='en')
        print(result)
    
root = tk.Tk()
root.title('language translator app')
root.geometry('530x330')

t1 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=10,y=100)
t2 = Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=260,y=100)
button = Button(root,text="Translate",relief=RIDGE,borderwidth=3,
                font=('verdana',10,'bold'),cursor="hand2",command=translate)
button.place(x=150,y=280)

button = Button(root,text="Speech Recognizer",relief=RIDGE,borderwidth=3,
                font=('verdana',10,'bold'),cursor="hand2",command=speech_demo)
button.place(x=300,y=280)
root.mainloop()
