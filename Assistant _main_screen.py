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
from tkinter import messagebox


root = Tk()
root.title('Siri')
root.geometry('500x500')
root.focus_set()            
label_pic = PhotoImage(file="sheela1.gif")
#icon = PhotoImage(file=r"C:\Program Files\AppData\logo.png")
#root.iconphoto(False,icon)
demo=Label(root,image=label_pic,width=350,height=100)
photo = PhotoImage(file="sheela1.gif")
gif_index = 0


class reco():
    def hello1():
        freq = 44100
        duration = 10
        recording = sd.rec(int(duration * freq), 
			samplerate=freq, channels=2) 
        sd.wait(200) 
        wv.write(r"C:\Program Files\AppData\assistantdata.wav", recording, freq, sampwidth=1)
        r=sr.Recognizer()
        file=sr.AudioFile(r'C:\Program Files\AppData\assistantdata.wav')
        with file as source:
            r.adjust_for_ambient_noise(source)
            audio=r.record(source, duration=10)
            result=r.recognize_google(audio,language='en')
        return result


def next_frame():
        
    global gif_index
    try:
        
        photo.configure(format="gif -index {}".format(gif_index))
        gif_index += 1
    except TclError:
        gif_index = 0
        return next_frame()
    else:
        root.after(22, next_frame) 
label1 = Label(root, image=photo,width=350,height=300)
label1.place(x=0,y=0)
root.after_idle(next_frame)

def start():
    try:
        result = reco.hello1()
        outbox.insert(END,"\n"+result)
        result=result.lower()
        engine = pyttsx3.init()  

        note='notepad'
        if note in result:
            
            engine. setProperty("rate", 150)
            engine.say('opening Notepad')
            engine.runAndWait()
            outbox.insert(END,'\nopening Notepad')
            os.system('cmd /c notepad.exe')

        command='control panel'
        if command in result:
            engine. setProperty("rate", 150)
            engine.say(' ok here we go, launching control panel')
            engine.runAndWait()
            os.system('cmd /c control.exe')
            
        command='music'
        if command in result:
            os.system('cmd /c start wmplayer.exe')
        
        command='shut down'
        if command in result:
            engine.say("alright shutting down")
            engine.runAndWait()
            os.system('cmd /c shutdown /s /t 10 ')
            
        command='chrome'
        if command in result:
	        os.system('cmd /c start chrome.exe')
            
        command='location'
        if command in result:
            engine. setProperty("rate", 150)
            import geocoder
            g = geocoder.ip('me')
            curlocation = g.city
            outbox.insert(END,"\nSiri>> your current location is "+curlocation)
            engine.say("your current location is :"+curlocation)
            engine.runAndWait()

        command='search'
        if command in result:
            
            engine. setProperty("rate", 150)
            engine.say('now speak to search the results')
            engine.runAndWait()
            result = reco.hello1()
            try:
	            from googlesearch import search
            except ImportError:
	            print("No module named 'google' found")
            query = result
            outbox.insert(END,"\nSiri>> searched for\n"+query)
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                outbox.insert(END,"\nSiri>> results are \n"+j)

        command="weather"
        if command in result:
            import requests, json 
            engine.say("City name :")
            engine.runAndWait()
            city = reco.hello1()
            api_key = "caac4a5d68b34cf32837beb33d725529"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            url = base_url+"appid="+api_key+"&q="+city
            response = requests.get(url)
            x = response. json()
            if x['cod']!=401:
                outbox.insert(END,"\n"+str(("City Name : ", x['name'])))
                outbox.insert(END,"\n"+str(("Weather: ",x['weather'])))
                outbox.insert(END,"\n"+str(("Weather: ", x['weather'][0]['main'])))
                outbox.insert(END,"\n"+str(("Temp : ", x['main']['temp'])))
                outbox.insert(END,"\n"+str(("Minimum Temp : ", x['main']['temp_min'])))
                outbox.insert(END,"\n"+str(("Max Temp : ", x['main']['temp_max'])))
                              
            else: 
                outbox.insert(END,"City ot found")
                    
                
        command='translate'
        if command in result:
            engine. setProperty("rate", 150)        
            engine.say('here is your translator')
            engine.runAndWait()    
            

    except sr.UnknownValueError:
        messagebox.showerror("Retry!","Didn't Understand that please retry!")
    except sr.RequestError:
        messagebox.showerror("Connect to Internet !","Make sure you are connected to internet and then try again")
startbtn = Button(root,text='Start Listening',command=start)
startbtn.place(x=140,y=400)
outbox = Text(root,height = 5,width =80,font=('Calbri',10))
outbox.place(x=0,y=310)
outbox.insert("1.0","Siri>>")
root.mainloop()


