from speech_recognition import Microphone,Recognizer,UnknownValueError,RequestError

from tkinter import messagebox
recognizer = Recognizer()
def voice_command():
    microphone_ = Microphone()
    try :
        with microphone_:
            audio = recognizer.listen(microphone_)

        text = recognizer.recognize_google(audio)

        text_l = text.lower()
        if text_l == "select document":
            command = "select_document"
        elif text_l == "generate report":
            command = "generate_report"
        elif text_l == "exit":
            command = "exit"
        elif text_l == "analysis history":
            command = "read_analysis"
        else:
            command = "unknown"
        return command
    except UnknownValueError:
        show_message("UnKnown Command")
    except RequestError:
        show_message("Not connected to internet")
    except OSError:
        show_message("Microphone Error Occurred")

def show_message(message, title="VoiceDoc"): #to display error on GUI
    messagebox.showwarning(title,message)