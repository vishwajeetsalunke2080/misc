from pytesseract import pytesseract
from tkinter import Tk
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
import os
from PIL import Image

#root initialization
root= Tk()
root.geometry('1100x550')
root.title("Tesseract OCR")

#function definitions
def helpinfo():
    messagebox.showinfo("About","Tesseract OCR"+"\n"+"Powered by © Tesseract"+"\n"+"Help & Support: vishwajeetsalunke42@outlook.com")

def browse_file():   
    try:
        file = askopenfilename(defaultextension=".png", 
                                filetypes=[("Portable Network Graphics File",".png")])  
        if file == "":  
            file = None
        else: 
            root.title("Tesseract OCR - "+os.path.basename(file)) 
            file = open(file,"r") 
            image=file.name
            
            text1.delete('1.0',END)
            text1.insert("1.0",image)
            file.close()
    except UnicodeDecodeError:
        messagebox.showerror("Error!","Image not Supported")
    image_path = image
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"	
    img = Image.open(image_path) 
    pytesseract.tesseract_cmd = path_to_tesseract 
    text = pytesseract.image_to_string(img) 
    textbox.delete('1.0',END)    
    textbox.insert("1.0",text[:-1])

#input components [textbox,labels]
textbox = Text(root,width=100,height=25,font=('Calbri',12))
textbox.pack()
text1 = Text(root,width=100,height=1,font=('Calbri',12))
text1.pack()
label = Label(root,text="Image Path :")
label.place(x=10,y=450)

#menu Components
my_menu=Menu(root)
root.config(menu=my_menu)
file_menu= Menu(my_menu)
my_menu.add_cascade(label="Help", menu=file_menu)
file_menu.add_command(label="About",command=helpinfo)

#button components
button1 = Button(root,text="Browse",command=browse_file)
button1.place(x=470,y=500)
root.mainloop()