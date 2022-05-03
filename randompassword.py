import tkinter as tk
from tkinter import *
from camelcase import CamelCase
import random 

root = tk.Tk()
root.title('random password generator')
password = Text(root,width=20,height=2)
password.pack()
finalpass = ""
def generate_password():
    special = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(8):
        someint = random.randint(0,3)
        if(someint == 0):
            someint = random.randint(0,9)
            finalpass = finalpass+numbers[someint]
        elif(someint == 1):
            someint = random.randint(0,13)
            finalpass = finalpass+special[someint]
        elif(someint == 2):
            someint = random.randint(0,25)
            finalpass = letters[someint]+finalpass
        elif(someint == 3):
            someint = random.randint(0,25)
            finalpass = finalpass+capletters[someint]

    print(finalpass)

generate = Button(root,text = 'Generate Password',command=generate_password)
generate.pack(side =LEFT)
root.mainloop()
