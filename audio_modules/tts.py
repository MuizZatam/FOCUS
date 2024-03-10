import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume',1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def sayText(text):

    engine.say(text)
    engine.runAndWait()
    engine.stop()
    return text
