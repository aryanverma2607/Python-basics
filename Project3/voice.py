import pyttsx3

def speak(text): #ye function engine ka object banaega new har bar function call ek time
    engine=pyttsx3.init()

    voices = engine.getProperty("voices")

    engine.setProperty("voice",voices[2].id)

# engine.say("Hello,Cutie")
# engine.runAndWait()

# def speak(text):
    engine.say(text)
    engine.runAndWait()

