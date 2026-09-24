import language_tool_python
from tkinter import filedialog

def open_file():
    file_type=[('text files','*.txt'),('All files','*.*')]
    path = filedialog.askopenfilename(
        filetypes=file_type
        )
    if path=='':
        return "No File Selected"
    else:
        return path

def select_document():   #document Selected
    a=open_file()   #to get path of document
    with open(a,"r") as y:     #file handling - open file path
        text=y.read()     #complete file content read karta hai,readline()-single line read karta hai,readlines=multiple lines read karega or list mein store karega
    # print(text)    #reading text of file

    ch_count=len(text)
    word=text.split()
    lines=text.splitlines()   #this split text line by line

    count1=0
    for i in range(len(text)):
        if text[i]=="." or text[i]=="?" or text[i]=="!":
            count1+=1

    return ch_count,len(word),len(lines),count1,text
