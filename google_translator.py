#necessary Imports 
import setuptools
from gtts import gTTS
import tkinter as tk
from scipy.io.wavfile import write 
import json
from googletrans import Translator
import wavio as wv
from tkinter import messagebox
from tkinter import ttk
import sounddevice as sd
from tkinter import *
import os
from os import path
import speech_recognition as sr
from tkinter.messagebox import *
from tkinter.filedialog import *
import requests
from playsound import playsound


#root initialization
root=tk.Tk()
root.title("Google Translate")
root.geometry('1000x500')


#arrays for language selection
gtts = ['af', 'ar', 'bn', 'bs', 'ca', 'cs', 'cy', 'da',
'de', 'el', 'en', 'eo', 'es', 'et', 'fi', 'fr', 'gu', 'hi',
'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jw', 'km', 'kn',
'ko', 'la', 'lv', 'mk', 'ml', 'mr', 'ne', 'nl', 'no', 'pl',
'pt', 'ro', 'ru', 'si', 'sk', 'sq', 'sr', 'su', 'sv', 'sw',
'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi']


#functions of program
def Translation_Function():
    try:
        translator_input = user_input_textbox.get("1.0","end")
        translator = Translator()
        source = translator.detect(translator_input)
        source_lang.set(source[1])
        src=source_lang.current()
        source = gtts[src]
        dst=dest_lang.current()
        destination = gtts[dst]
        translation = translator.translate(translator_input,lang_src=source,lang_tgt=destination)
        answer_textbox.delete('1.0',END)
        answer_textbox.insert("1.0",translation)
        
        
    except Exception as e:
        print(e)
    
   
def info():
    messagebox.showinfo("Version","Version 1.1"+"\n"+"Google Translate (2021-22)"+"\n"+"help & support : vishwajeetsalunke42@outlook.com")    

def open_file():
    try:
        file = askopenfilename(defaultextension=".txt", 
                                  filetypes=[("Text Documents",".txt")])  
        if file == "":   
            file = None
        else: 
            root.title("Google Translate - "+os.path.basename(file)) 
            user_input_textbox.delete(1.0,END)   
            file = open(file,"r") 
            user_input_textbox.insert(1.0,file.read())   
            file.close()
    except Exception:
        messagebox.showerror("Error!","Only English Language Supported")


def exchange_command():
    t2 = answer_textbox.get("1.0",END)
    answer_textbox.delete("1.0",END)
    user_input_textbox.delete("1.0",END)
    user_input_textbox.insert("1.0",t2) 

def speaker_output_answer():
    try:
        translator_input = user_input_textbox.get("1.0","end")
        translator = google_translator()
        source = translator.detect(translator_input)
        source_lang.set(source[1])
        src=source_lang.current()
        source = gtts[src]
        dst=dest_lang.current()
        destination = gtts[dst]
        translation = translator.translate(translator_input,lang_src=source,lang_tgt=destination)
        myobj = gTTS(text=translation, lang=destination, slow=False) 
        myobj.save(path.expandvars(r"%AppData%\Translation.mp3"))
        playsound(path.expandvars(r"%AppData%\Translation.mp3"))
        os.remove(path.expandvars(r"%AppData%\Translation.mp3"))
    except Exception:
        messagebox.showerror("Error!","some connection error occured")

def speaker_output_src():
    try:
        translator_input = user_input_textbox.get("1.0","end")
        translator = google_translator()
        source = translator.detect(translator_input)
        source_lang.set(source[1])
        myobj = gTTS(text=translator_input, lang=source[0], slow=False) 
        myobj.save(path.expandvars(r"%AppData%\Translation.mp3"))
        playsound(path.expandvars(r"%AppData%\Translation.mp3"))
        os.remove(path.expandvars(r"%AppData%\Translation.mp3"))
    except Exception:
        messagebox.showerror("Error!","some connection error occured")

#menu objects
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu= Menu(my_menu)

my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open File",command=open_file)

file_menu.add_command(label="Exit",command=root.quit)
about_menu= Menu(my_menu)
my_menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Version",command=info)

#input objects
user_input_textbox = Text(root,width=50,height=20,font=('calbri',11))
user_input_textbox.place(x=50,y=60)
answer_textbox = Text(root,width=50,height=20,font=('calbri',11))
answer_textbox.place(x=550,y=60)

#choice objects
n = tk.StringVar()
source_lang = ttk.Combobox(root,width=10,text=n)
source_lang['values']=('Afrikaans', 'Arabic', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Welsh',
'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Finnish', 'French',
'Gujarati', 'Hindi', 'Croatian', 'Hungarian', 'Armenian', 'Indonesian', 'Icelandic', 'Italian',
'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Malayalam',
'Marathi', 'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Sinhala',
'Slovak', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai',
'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese')
source_lang.grid(column=5,row=5)
source_lang.place(x=165,y=20)
source_lang.set("Auto-Detect")
n1 = tk.StringVar()
dest_lang = ttk.Combobox(root,width=10,text=n1)
dest_lang['values']=('Afrikaans', 'Arabic', 'Bengali', 'Bosnian', 'Catalan', 'Czech', 'Welsh',
'Danish', 'German', 'Greek', 'English', 'Esperanto', 'Spanish', 'Estonian', 'Finnish', 'French',
'Gujarati', 'Hindi', 'Croatian', 'Hungarian', 'Armenian', 'Indonesian', 'Icelandic', 'Italian',
'Japanese', 'Javanese', 'Khmer', 'Kannada', 'Korean', 'Latin', 'Latvian', 'Macedonian', 'Malayalam',
'Marathi', 'Nepali', 'Dutch', 'Norwegian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Sinhala',
'Slovak', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai',
'Filipino', 'Turkish', 'Ukrainian', 'Urdu', 'Vietnamese')
dest_lang.grid(column=1,row=5)
dest_lang.place(x=695,y=20)
dest_lang.set("Hindi")


#button objects
Translate_button = Button(root,text='Translate',command=Translation_Function)
Translate_button.place(x=360,y=430)


exchange = Button(root,command=exchange_command)
exchange.place(x=490,y=230)
speak_btn = Button(root,command=speaker_output_answer)
speak_btn.place(x=930,y=410)
speak_btn1 = Button(root,command=speaker_output_src)
speak_btn1.place(x=50,y=410)
#label objects
label_1 = Label(root,text="Source Language :")
label_1.place(x=48,y=20)
label_2 = Label(root,text="Destination Language :")
label_2.place(x=550,y=20)

#root
root.mainloop()
