# it is updated version of Tkinter
# it is used to modern GUI and provide with better styling
# it is user-defined module

'''Normal Tkinter       CustomTkinter
─────────────        ─────────────
Button               CTkButton
Label                CTkLabel
Entry                CTkEntry
Frame                CTkFrame
Checkbutton          CTkCheckBox
Radiobutton          CTkRadioButton'''

from customtkinter import *


app = CTk(fg_color="pink")   #fg_color =background color

app.title("VoiceDoc")
app.geometry("500x400+700+200")
app.resizable(True,True)           #it allow to resize the window or not
app.maxsize(height=650,width=650)   #to fixed the window maximum size
app.minsize(height=200,width=200)   #to fixed the window minimum size


l1=CTkLabel(app,text="VoiceDoc",text_color="red",fg_color="yellow",corner_radius=10,font=("Courier",24),border_color="blue")  #to add label or widgets to our window 
# corner_radius - widget ko ek well shape mein display karta hai
# we can change color of widget and also text color
# height,width can also be given in CTklabel(height=,width=)
#l1.pack(expand=False,fill="x",)         # it will show output if not packed then output will not shown
# l1.place(x=0,y=0)
# if expand = true it will add widget or label on the center by default False hota hai
# fill the window header with the given axis only x,y
name = StringVar(value="Aryan")      #takes string input, label ke pehle variable define karna padega
phone = IntVar(value=21)
dec = DoubleVar(value=1.244)
bol = BooleanVar(value=0)
# we can update values using set()
name.set("Hello Niteen")        #we can update value of variable using set()
#kisi bhi widget ya label mein hum variable de sakte hai
l2=CTkLabel(app,text=name.get(),text_color="red",fg_color="yellow",corner_radius=1,font=("Courier",24),border_color="blue") #anchor - it move text inside widget and takes direction as arguement
#l2.pack(fill="x")
# variable ki value lene ke liye get() use karenge


#to take input using button
username = CTkEntry(app,height=30,width=200,fg_color="white",text_color="Black",placeholder_text="Username")
username.grid(row=3,column=0)         #Position decidev karega
password = CTkEntry(app,height=30,width=200,fg_color="white",text_color="Black",placeholder_text="Password")
password.grid(row=4,column=0)

# password = CTkEntry(app,textvariable=name.get(),height=30,width=200,fg_color="white",text_color="Black",placeholder_text="Password")
# password.grid(row=6,column=0)

#variable definition
name="Aryan"  #not valid in customtkinter

#function is called before button
def hello():
    print("Hello Aryan!!!")
    print(username.get())   #it will return input given in the input box
    print(password.get())   #to get values
#grid=window ko row and column ke jese dekhta hai
l1.grid(row=0,column=0,padx=10,pady=10)
l2.grid(row=1,column=0)
#l2.place(x=0,y=25)   #it requires coordinate to place widgets
btn =CTkButton(app,text="Submit",fg_color="black",text_color="green",command=hello,hover_color="white",cursor="hand2",height=30,width=100)
#CTkbutton(window_name,Text,Function_name)
btn.grid(row=5,column=0)


app.mainloop()
