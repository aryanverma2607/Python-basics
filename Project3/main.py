#jay Sanwariya Seth ki
from customtkinter import *
from Document import open_file,select_document
from Grammar import grammar_check
from voice import speak



app = CTk(fg_color="Pink")
app.geometry("700x900")
app.resizable(True,True)

main_frame=CTkScrollableFrame(app,fg_color="pink")
main_frame.pack(fill="both",expand=True)


header=CTkFrame(main_frame,fg_color="white",corner_radius=15)
header.pack(fill="x",padx=40,pady=(30,20))


label1=CTkLabel(header,
text="VoiceDoc",
text_color="#222222",
fg_color="white",
corner_radius=3,
font=("Courier",32))

label1.pack(fill="x")

label2=CTkLabel(header,
                text="Voice Controlled Document Analyzer",
                text_color="#666666",
                fg_color="white",
                corner_radius=3,
                font=("Courier",24)
                )
label2.pack(fill="x")

def hello():
    print("Aryan")

button1=CTkButton(main_frame,text="🎙️ Voice Command",command=hello,fg_color="White",text_color="black",hover_color="#1AB1F2",font=("courier",18,"bold"))
button1.pack(padx=20,pady=20)

def select_button():
    voice_message=[]
    character,words,line,sentence,text=select_document()
    check=grammar_check(text)
    result_box.delete("1.0","end")    #it clear content box after new document selection
    for i,r in enumerate(check, start=1):   #give numbering to the error
        error_message="Error"+" "+str(i) + "\n"
        result_box.insert("end",error_message)
        #speak(error_message)
        category="Type:"+ str(r["category"]) + "\n"
        result_box.insert("end",category)
        message="Problem:"+str(r["message"]) + "\n"
        result_box.insert("end",message)
        #speak(message)
        replace = "Suggestion: " + ", ".join(r["replacements"]) + "\n"
        result_box.insert("end",replace)
        result_box.insert("end","-" * 60 + "\n\n")
        result_box.update()
        voice=(error_message + " " + message + " " + replace)
        voice_message.append(voice)
    for message in voice_message:
        speak(message)








        # result_box.insert("end",f"Error {i}\n")    #number of error
        # result_box.insert("end",f"type: {r["category"]}\n")      #category of error
        # result_box.insert("end",f"Problem: {r["message"]}\n")    #explanation of problem
        # result_box.insert("end",f"Suggestion: {",".join(r["replacements"])}\n")     #Suggested Corrections
        # result_box.insert("end","-" * 60 + "\n\n")   #error seperator

    content_box.delete("1.0", "end")  #it clear content box after new document selection
    content_box.insert("1.0", text)
    label_count.configure(text="Character Count:" + str(character))  #changes existing labels
    #label_count.pack(pady=3)

    label_words.configure(text="Words Count:" + str(words))
    #label_words.pack(pady=3)

    label_lines.configure(text="Lines Count:" + str(line))
    #label_lines.pack(pady=3)

    label_sentence.configure(text="Sentence Count:" + str(sentence))
    #label_sentence.pack(pady=(3,15))
    label_count.pack(side="left", padx=20, pady=10)
    label_words.pack(side="left", padx=20, pady=10)

    label_lines.pack(side="left", padx=20, pady=10)
    label_sentence.pack(side="left", padx=20, pady=10)

    analysis_frame.pack(fill="x",padx=40,pady=10,before=button3)    #ye analysis_frame for button 3 ke pehle display karega 
#otherwise sabse niche display karega
    speak(f"“Document analysis completed. The document contains {character} characters, {words} words, {line} lines, {sentence} sentences, and {len(check)} grammar errors.”")

document_frame=CTkFrame(
    main_frame,
    fg_color="white",
    corner_radius=15
    )

document_frame.pack(fill="x",padx=0,pady=10)

content_title = CTkLabel(document_frame,
                        text="Document Content",
                        text_color="black",
                        font=("courier",18,"bold")
                        )
content_title.pack(pady=(15,5))

content_box = CTkTextbox(document_frame,
                        height=200,
                        width=600,
                        text_color="black",
                        fg_color="white",
                        border_width=1,
                        border_color="#cccccc",
                        font=("courier",13)
                        )

content_box.pack(padx=20,pady=(5,20))


button2=CTkButton(document_frame,
                text="📄 Select Document",
                command=select_button,
                height=50,
                width=50,
                font=("Courier",18,"bold"),
                fg_color="White",
                text_color="black",
                corner_radius=10,
                hover_color="#1AB1F2")
button2.pack(padx=20,pady=20)


analysis_frame=CTkFrame(main_frame,
                        fg_color="white",
                        corner_radius=15)
# analysis_frame.pack_forget()
#analysis_frame.pack(fill="x",padx=40,pady=10)
analysis_frame.pack_forget()

analysis_title=CTkLabel(analysis_frame,text="📊 Document Analysis",text_color="#222222",font=("Courier",20,"bold"))
analysis_title.pack(pady=(15,10))

row1=CTkFrame(analysis_frame,fg_color="transparent")
row1.pack(pady=5)

row2=CTkFrame(analysis_frame,fg_color="transparent")
row2.pack(pady=5)

label_count=CTkLabel(row1,text="Character Count:",text_color="black",font=("Courier",18))

label_words=CTkLabel(row1,text="Words Count:",text_color="black",font=("Courier",18))

label_lines=CTkLabel(row2,text="Lines Count:",text_color="black",font=("Courier",18))

label_sentence=CTkLabel(row2,text="Sentence Count:",text_color="black",font=("Courier",18))

Grammar_analysis=CTkLabel(
    analysis_frame,
    text="📝 Grammar Analysis",
    text_color="black",
    fg_color="white",
    font=("courier",20,"bold")
    )
Grammar_analysis.pack(fill="x",padx=20,pady=20)

result_box=CTkTextbox(
    analysis_frame,
    height=200,
    width=600,
    text_color="black",
    fg_color="white",
    font=("courier",13)
)
result_box.pack(
    padx=20,
    pady=(5,20)
)


button3=CTkButton(main_frame,text="📊 Analysis History",command=hello,fg_color="White",text_color="black",hover_color="#1AB1F2",font=("courier",18,"bold"))
button3.pack(padx=20,pady=20)

button4=CTkButton(main_frame,text="❌ Exit",command=app.destroy,fg_color="White",text_color="black",hover_color="#1AB1F2",font=("courier",18,"bold"))
button4.pack(padx=20,pady=20)


app.mainloop()
