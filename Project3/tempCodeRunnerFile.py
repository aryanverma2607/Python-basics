from speech_recognition import Microphone,Recognizer

recognizer = Recognizer()

microphone_ = Microphone()
with microphone_:  #it activate microphone
    audio = recognizer.listen(microphone_)    #it allow Microphone to listen

text = recognizer.recognize_google(audio)
print(text)

