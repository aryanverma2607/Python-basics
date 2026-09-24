#Python ka GUI library hai--terminal ki jagah ek actual window:
import tkinter as tk

a=tk.Tk("Student data")  #Sabse pehle main window create hoti hai
print(a)
a.mainloop() #Window create karne ke baad program ko continuously window ko listen karna hota hai.
a.title("Student information")  #window title

a.geometry("100x200") #Window size width x  height

label=tk.Label(a,text="Aryan singh") #Label ka use text display karne ke liye hota hai
'''
layout managers:
pack()
grid()
place()
'''
label.pack()

button = tk.Button(a, text="Submit") #Button user ko click karne ka option deta hai.
button.pack()

def submit():
    print("Submitted")
command = submit

#entry - user se single input lene ke liye
#text - for multiple input from user
entry = tk.Entry(a)
entry.pack()

entry.get() #to access input
Text.get()

entry.delete() #to delete input

#checkbutton - to select one or more option

#radiobutton - to select one button

#frame - to group multiple program or it organize large GUI very well
#grid() - Rows aur columns ke form me widgets arrange karta hai.
#place() - to specify position

#messagebox - popup message show karne ke liye
from tkinter import messagebox

'''Important functions
showinfo()
showwarning()
showerror()
askyesno()'''

#Combobox - Dropdown menu like interface
from tkinter import  ttk

#Listbox - Multiple items ki list display karne ke liye.

