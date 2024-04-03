import pyttsx3

engine = pyttsx3.init()

text = input("type what you want to listen: ")

engine.say(text)

engine.runAndWait()