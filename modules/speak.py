import pyttsx3

def speak(text):
    engine = pyttsx3.init()   #creating a local engine instead of using a global one to avoid conflicts
    engine.say(text)
    engine.runAndWait()
    engine.stop()