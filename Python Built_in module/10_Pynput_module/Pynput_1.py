# Pynput is mainly used to control or monitor  keyboard or mouse programmatically
# it is user-defined module and requires installation
from pynput import mouse  #for mouse
from pynput import keyboard   #for keyboard

'''Using Pynput :
we can control mouse move,left/right,or scroll'''

from pynput.mouse import Controller , Button
import time
mouse = Controller()

mouse.position = (900,300)  #(X-coordinate,Y-coordinate) actual mouse cursor screen par (500, 300)
mouse.click(Button.right)   #jis location par cursor gaya, wahan left click hoga
time.sleep(3)
mouse.click(Button.left,2)   #it allow left click for 2 times
time.sleep(3)
mouse.scroll(0,2)   #Up Scroll
time.sleep(3)
mouse.scroll(-1,-2)   #down scroll
from pynput.keyboard import Controller

keyboard=Controller()
time.sleep(3)
keyboard.type("Hello")

'''
from pynput.keyboard import Key

keyboard.press(Key.enter)
keyboard.release(Key.enter)
'''



'''
Important Key:
Key.enter
Key.space
Key.tab
Key.esc
Key.backspace
Key.shift
Key.ctrl
Key.alt '''
