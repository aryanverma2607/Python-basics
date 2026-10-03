import python_inspector
from python_inspector.voice import speak

path = input("Enter your Python project path: ")

python_inspector.inspect(path)

speak("Python Inspector analysis completed successfully")