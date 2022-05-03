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
#all arrays
start_array = ["Afrikaans","Arabic","Bengali","Bosnian","Catalan","Welsh","Danish",
"German","Greek","English","Esperanto","Spanish","Estonian","Finnish","French",
"Gujarati","Hindi","Croatian","Hungarian","Armenian","Indonesian","Icelandic","Italian",
"Japanese","Javanese","Khmer","Kannada","Korean","Latin","Latvian","Macedonian",
"Malayalam","Marathi","Myanmar","Nepali","Dutch","Norwegian","Polish","Portuguese","Romanian",
"Russian","Sinhala","Slovak","Albanian","Serbian","Sundanese","Swedish","Swahili","Tamil",
"Telugu","Thai","Filipino","Turkish","Ukrainian","Urdu","Vietnamese"]

dest_ar = ["Afrikaans","Arabic","Bengali","Bosnian","Catalan","Welsh","Danish",
"German","Greek","English","Esperanto","Spanish","Estonian","Finnish","French",
"Gujarati","Hindi","Croatian","Hungarian","Armenian","Indonesian","Icelandic","Italian",
"Japanese","Javanese","Khmer","Kannada","Korean","Latin","Latvian","Macedonian",
"Malayalam","Marathi","Myanmar","Nepali","Dutch","Norwegian","Polish","Portuguese","Romanian",
"Russian","Sinhala","Slovak","Albanian","Serbian","Sundanese","Swedish","Swahili","Tamil",
"Telugu","Thai","Filipino","Turkish","Ukrainian","Urdu","Vietnamese"]

gtts_langs = ['af','ar','bn','bs','ca','cs','cy','da','de','el','en',
'eo','es','et','fi','fr','gu','hi','hr','hu','hy','id','is','it','ja',
'jw','km','kn','ko','la','lv','mk',"ml",'mr','my','ne','nl','no','pl'
,'pt','ro','ru','si','sk','sq','sr','su','sv','sw','ta','te','th','tl'
,'tr','uk','ur','vi']



def Translation_Function():
    translator_input = user_input_textbox.get("1.0","end")
    src=source_lang.get()
    dst=dest_lang.get()
    feed1 = dest_ar.index(dst)
    feed = gtts_langs[feed1+1]
    start1 = start_array.index(src)
    starts = gtts_langs[start1+1]
    translator = google_translator()
    translation = translator.translate(translator_input,lang_src=starts,lang_tgt=feed)
    answer_textbox.delete('1.0',END)
    answer_textbox.insert("1.0",translation)
    
    myobj = gTTS(text=translation, lang=feed, slow=False) 
    myobj.save(r"D:\welcome.mp3")
    os.system(r"D:\welcome.mp3")
    
#main container 

root=tk.Tk()
root.title("Google Translator")
root.geometry('1000x240')
icon = PhotoImage(file=r"C:\Users\vishw\Downloads\gt.png")
root.iconphoto(False,icon)
my_menu=Menu(root)
root.config(menu=my_menu)
#img = PhotoImage(file = r"C:\Users\vishw\Downloads\gt.png") 
#photoimage=img.subsample(10,10)
#label = Label(image = photoimage)
#label.place(x=350,y=0)
def open_file():
    messagebox.showinfo("Warning !!","Please make sure :"+"\n"+"~ File should be in .txt format"+"\n"+"~ File should not exceed 500 characters"+"\n"+"~ Else only 500 characters will be displayed")
    file = askopenfilename(defaultextension=".txt", 
                                  filetypes=[("All Files","*.*"), 
                                      ("Text Documents","*.txt")]) 
  
    if file == "": 
  
        # no file to open 
        file = None
    else: 
        # try to open the file 
        # set the window title 
        #root.title(os.path.basename(file)) 
        user_input_textbox.delete(1.0,END) 
  
        file = open(file,"r") 

        user_input_textbox.insert(1.0,file.read()) 
  
        file.close()

file_menu= Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File",command=open_file)

file_menu.add_command(label="Exit",command=root.quit)


user_input_textbox = Text(root,width=50,height=5,font=('calbri',11))
user_input_textbox.place(x=50,y=60)
answer_textbox = Text(root,width=50,height=5,font=('calbri',11))
answer_textbox.place(x=550,y=60)
'''
pronounciation = Button(root,text='Pronounciation',width=13,height=1,command=pro)
pronounciation.place(x=500,y=170)
'''
Translate_button = Button(root,text='Translate',width=10,height=1,command=Translation_Function)
Translate_button.place(x=400,y=170)
label_1 = Label(root,text="Source Language :")
label_1.place(x=50,y=20)
label_2 = Label(root,text="Destination Language :")
label_2.place(x=550,y=20)

n = tk.StringVar()
source_lang = ttk.Combobox(root,width=10,text=n)
source_lang['values']=("Afrikaans","Arabic","Bengali","Bosnian","Catalan","Welsh","Danish",
"German","Greek","English","Esperanto","Spanish","Estonian","Finnish","French",
"Gujarati","Hindi","Croatian","Hungarian","Armenian","Indonesian","Icelandic","Italian",
"Japanese","Javanese","Khmer","Kannada","Korean","Latin","Latvian","Macedonian",
"Malayalam","Marathi","Myanmar","Nepali","Dutch","Norwegian","Polish","Portuguese","Romanian",
"Russian","Sinhala","Slovak","Albanian","Serbian","Sundanese","Swedish","Swahili","Tamil",
"Telugu","Thai","Filipino","Turkish","Ukrainian","Urdu","Vietnamese")

source_lang.grid(column=5,row=5)
source_lang.place(x=165,y=20)
source_lang.set("English")
n1 = tk.StringVar()
dest_lang = ttk.Combobox(root,width=10,text=n1)
dest_lang['values']=("Afrikaans","Arabic","Bengali","Bosnian","Catalan","Welsh","Danish",
"German","Greek","English","Esperanto","Spanish","Estonian","Finnish","French",
"Gujarati","Hindi","Croatian","Hungarian","Armenian","Indonesian","Icelandic","Italian",
"Japanese","Javanese","Khmer","Kannada","Korean","Latin","Latvian","Macedonian",
"Malayalam","Marathi","Myanmar","Nepali","Dutch","Norwegian","Polish","Portuguese","Romanian",
"Russian","Sinhala","Slovak","Albanian","Serbian","Sundanese","Swedish","Swahili","Tamil",
"Telugu","Thai","Filipino","Turkish","Ukrainian","Urdu","Vietnamese")

dest_lang.grid(column=1,row=5)
dest_lang.place(x=695,y=20)
dest_lang.set("Hindi")
root.mainloop()
