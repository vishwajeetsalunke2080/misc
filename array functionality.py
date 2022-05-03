import tkinter as tk
from gtts import gTTS
#from tempfile import TemporaryFile
from google_trans_new import google_translator
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import os
import speech_recognition as sr
from tkinter.messagebox import *
from tkinter.filedialog import *
import webbrowser

root = Tk()
root.geometry('1000x1000')

url_list = Listbox(root,width=50,height=5)
url_list.place(x=100,y=100)



def getresults():
    
    try:
	    from googlesearch import search
    except ImportError:
	    print("No module named 'google' found")

    
    # to search
    query = text1.get('1.0',END)
    url_list.delete(END)
    for j in search(query):
        url_list.insert(END,j)
    text1.delete('1.0',END)
    

def onclick():
    
    url = url_list.get(url_list.curselection())
    webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
    webbrowser.get('chrome').open_new(url)



text1 = Text(root,width=20,height=1)
text1.place(x=100,y=0)
button = Button(root,text='open url',command=onclick)
label = Label(root,text='Search Here :')
label.place(x=0,y=0)
button.place(x=100,y=30)
get_result = Button(root,text='get result',command=getresults)
get_result.place(x=200,y=30)
root.mainloop()