import eel
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 125)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


@eel.expose
def tts(text):

    engine.say(text)
    engine.runAndWait()
    engine.stop

@eel.expose
def basicInfo(text):

    if text == "who are you":
        return "I am FOCUS, your very own friend designed to help you in your day to day tasks!"
    else:
        return "I didn't quite catch you..."
    
    
eel.init('frontend')
eel.start('index.html')