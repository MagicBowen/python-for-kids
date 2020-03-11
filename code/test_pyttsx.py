import pyttsx3

engine = pyttsx3.init()

def talk(str):
    engine.say(str)
    engine.runAndWait()

talk("Jerry，你猜的数字太大了")
talk("Jerry，你是个小孩子")

engine.stop()