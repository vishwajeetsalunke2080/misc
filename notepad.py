from tkinter import Tk
from tkinter import *
import os
from tkinter.filedialog import *
from tkinter import messagebox
root = Tk()
root.geometry('500x350')
root.title("Notepad")
text=Text(root,font=("Century Gothic",'10'))
text.pack()
select = []

def open_file():
    
    file = askopenfilename(defaultextension=".txt", 
                            filetypes=[("Text File",".txt"),("All Files","*")])  
    if file == "":   
        file = None
    else: 
        root.title("Notepad - "+os.path.basename(file)) 
        text.delete(1.0,END)   
        file = open(file,"r") 
        text.insert(1.0,file.read())   
        file.close()

def save_file():
    
    file = asksaveasfile(mode='w',defaultextension=".txt", 
                            filetypes=[("Text File",".txt"),("All Files","*")])  
    data = str(text.get('1.0',END))
    file.write(data)
    
    file.close

def copy():
    copied_text = text.get("1.0",END)
    select.insert(0,copied_text)
    
def paste():
    a = select[0]
    text.insert('1.0',a)

def set_font():
    from matplotlib import font_manager
    fonts = []
    for x in font_manager.win32InstalledFonts():
        x = x[::-1]
        dot = x.find('.')
        slash = x.find('\\')
        x = x[slash-1:dot:-1]
        fonts += [x]
        fonts.sort()
    n = tk.StringVar()
    source_lang = ttk.Combobox(root,width=10,text=n)
    source_lang['values']=("Auto-Detect")
    source_lang.grid(column=5,row=5)
    source_lang.place(x=165,y=20)
    source_lang.set("Auto-Detect")
    
        

my_menu=Menu(root)
root.config(menu=my_menu)
file_menu= Menu(my_menu)
edit_menu= Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Exit",command=root.quit)
edit_menu.add_command(label="Copy",command=copy)
edit_menu.add_command(label="Paste",command=paste)
edit_menu.add_command(label="Font",command=set_font)
root.mainloop()
