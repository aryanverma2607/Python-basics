'''import pyttsx3


engine=pyttsx3.init()


voices = engine.getProperty("voices")
for voice in voices:
    print(voice.id)
zira_id=r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty("voice",zira_id)
engine.say("Niteen")   #engine.say() text ko bolne ke liye use hota hai.
engine.runAndWait()
'''
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("voice", voices[1].id)

engine.say("Hello, I am Nitin.")
engine.runAndWait()