import pyttsx3
from tkinter import filedialog

filename = filedialog.askopenfilename()
file = open(filename,'r')

text = file.read()

text

play = pyttsx3.init()
print(text)


voices = play.getProperty('voices')
play.setProperty('voice', voices[1].id)

play.say(text)
play.runAndWait()

file.close()