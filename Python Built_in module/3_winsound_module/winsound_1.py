'''winsound Python ka Windows-specific built-in module hai.
Isse tum Windows computer me beep aur .wav sound files play kar sakte ho.'''
import winsound  #import

winsound.Beep(500,600)   #winsound.Beep(frequency, duration)
winsound.Beep(1000,300)
winsound.Beep(2000,300)
#winsound.PlaySound(r"C:\Users\ARYAN-VERMA\OneDrive\Desktop\huamain.wav", winsound.SND_FILENAME)  #(r"path in .wav format",winsound)  Playsound()-.wav audio file play karne ke liye
#SND_FILENAME - it plays the given string
winsound.PlaySound(r"C:\Users\ARYAN-VERMA\OneDrive\Desktop\jeene.wav",winsound.SND_FILENAME)

#SND_ASYNC
PlaySound() #sound finish hone tak program ko wait kara sakta hai.
winsound.PlaySound(
    "alert.wav",
    winsound.SND_FILENAME | winsound.SND_ASYNC
)

#SND_LOOP - to repeat/loop sound
winsound.PlaySound(
    "alert.wav",
    winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC
)
#to stop loop
winsound.PlaySound(None, winsound.SND_PURGE)

winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)