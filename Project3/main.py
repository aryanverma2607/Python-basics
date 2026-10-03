from customtkinter import CTkScrollableFrame,CTkButton,CTkLabel,CTkFrame,CTkTextbox,CTk
from Document import select_document
from Grammar import grammar_check
from voice import speak
from report import generate_report
from tkinter import filedialog
from voicecommand import voice_command,show_message

character=0
words=0
line=0
sentence=0
text=""
check=[]
correct=""
document_select=False


def voice_button():
    command = voice_command()
    
    if command == "select_document":
        select_button()

    elif command == "generate_report":
        if document_select==True:
            generate_report1(character,words,line,sentence,text,check,correct)
        else:
            show_message("Select document")

    elif command == "read_analysis":
        if document_select!=False:
            read_analysis()
        else:
            show_message("Select document")

    elif command == "exit":
        application_closed()
    elif command == "unknown":
        show_message("Unknown Command")

def generate_report1(character,words,line,sentence,text,check,correct):
    try:
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files","*.pdf")])
        if file_path!="":
            generate_report(character,words,line,sentence,text,check,correct,file_path)
    except PermissionError:
        show_message("PDF is not saved")
    except OSError:
        show_message("File or System error Occurred")
    except KeyError:
        show_message("Key is missing")
    except TypeError:
        show_message("Unexpected Data type")
    except ValueError:
        show_message("Invalid Value Provided")
def read_analysis():
    if document_select != False:
        speak("Total Character Count : " + str(character))
        speak("Total Words Count : " + str(words))
        speak("Lines Count : " + str(line))
        speak("Sentence Count : " + str(sentence))
        speak("Grammar Error Count : " + str(len(check)))

    else:
        show_message("Please Select A document First")


def application_closed():
    app.destroy()

app = CTk()
app.geometry("700x900")
app.resizable(True,True)

main_frame=CTkScrollableFrame(app,fg_color="#F9D2BA")
main_frame.pack(fill="both",expand=True)


header=CTkFrame(main_frame,fg_color="#F9D2BA",corner_radius=15)
header.pack(fill="x",padx=40,pady=(30,20))


label1=CTkLabel(header,
text="VoiceDoc",
text_color="#222222",
corner_radius=3,
font=("Times New Roman",32,"bold"))

label1.pack(fill="x")

label2=CTkLabel(header,
                text="Voice Controlled Document Analyzer",
                text_color="#222222",
                corner_radius=3,
                font=("Times New Roman",24,"bold")
                )
label2.pack(fill="x")


button1=CTkButton(main_frame,text="🎙️ Voice Command",command=voice_button,fg_color="White",text_color="black",hover_color="#1AB1F2",font=("courier",18,"bold"))
button1.pack(padx=20,pady=20)

def select_button():
    global document_select
    global character
    global words
    global line
    global sentence
    global text
    global check
    global correct
    
    document_select = True
    character,words,line,sentence,text=select_document()
    check,correct=grammar_check(text)
    result_box.delete("1.0","end")
    for i,r in enumerate(check, start=1):
        error_message="Error"+" "+str(i) + "\n"
        result_box.insert("end",error_message)
        
        category="Type:"+ str(r["category"]) + "\n"
        result_box.insert("end",category)

        message="Problem:"+str(r["message"]) + "\n"
        result_box.insert("end",message)
        
        replace = "Suggestion: " + ", ".join(r["replacements"]) + "\n"
        result_box.insert("end",replace)
        result_box.insert("end","-" * 60 + "\n\n")

    content_box.delete("1.0", "end")
    content_box.insert("1.0", text)
    label_count.configure(text="Character Count:" + str(character))

    label_words.configure(text="Words Count:" + str(words))

    label_lines.configure(text="Lines Count:" + str(line))

    label_sentence.configure(text="Sentence Count:" + str(sentence))


    label_count.pack(side="left", padx=20, pady=10)
    label_words.pack(side="left", padx=20, pady=10)

    label_lines.pack(side="left", padx=20, pady=10)
    label_sentence.pack(side="left", padx=20, pady=10)

    analysis_frame.pack(fill="x",padx=40,pady=10,before=button3)

    #speak(f"“Document analysis completed. The document contains {character} characters, {words} words, {line} lines, {sentence} sentences, and {len(check)} grammar errors.”")

    #return character,words,line,sentence,text,correct

document_frame=CTkFrame(
    main_frame,
    fg_color="#F9D2BA"
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
                        fg_color="#F3F4F4",
                        border_width=1,
                        border_color="#cccccc",
                        font=("courier",13)
                        )

content_box.pack(padx=20,pady=(5,20))


button2=CTkButton(document_frame,
                text="📄 Select Document",
                command=select_button,
                font=("Courier",18,"bold"),
                fg_color="White",
                text_color="black",
                corner_radius=10,
                hover_color="#1AB1F2")
button2.pack(padx=20,pady=20)


analysis_frame=CTkFrame(main_frame,
                        fg_color="#F3F4F4",
                        corner_radius=15)
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
    fg_color="#F3F4F4",
    font=("courier",20,"bold")
    )
Grammar_analysis.pack(fill="x",padx=20,pady=20)

result_box=CTkTextbox(
    analysis_frame,
    height=200,
    width=600,
    text_color="black",
    fg_color="#F3F4F4",
    font=("courier",13)
)
result_box.pack(
    padx=20,
    pady=(5,20)
)


button3=CTkButton(main_frame,text="📊 Analysis History",command=read_analysis,fg_color="White",text_color="black",hover_color="#1AB1F2",font=("courier",18,"bold"))
button3.pack(padx=20,pady=20)

def report_button():
    if document_select == True:
        generate_report1(character,words,line,sentence,text,check,correct)
    else:
        show_message("Please Select A Document First")

button5=CTkButton(main_frame,text="Generate Report",command=report_button,fg_color="White",text_color="black",hover_color="#1AB1F2",font=("courier",18,"bold"))
button5.pack(padx=20,pady=20)

button4=CTkButton(main_frame,text="❌ Exit",command=application_closed,fg_color="White",text_color="black",hover_color="#1AB1F2",font=("courier",18,"bold"))
button4.pack(padx=20,pady=20)

app.mainloop()
