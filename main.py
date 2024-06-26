import eel
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import webbrowser
import ollama

# Initialize Eel
eel.init('frontend')

# Initialize pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


@eel.expose
def tts(text):
    engine.say(text)
    engine.runAndWait()


@eel.expose
def greet():
    hour = datetime.datetime.now().hour
    greeting = "Good Morning!, Always Happy To Assist" if 0 <= hour < 12 else "Good Afternoon!, Always Happy To Assist" if 12 <= hour < 18 else "Good Evening!, Always Happy To Assist"
    tts(greeting)

@eel.expose
def basicInfo(text):
    
    if text.startswith("google"):
        returnVal = text.replace("google", "")
        try:
            result = wikipedia.summary(returnVal, sentences=1)
            pywhatkit.search(returnVal)
            tts(result)
            return result
        except Exception:
            pywhatkit.search(returnVal)
            tts("Unable to summarize, source not found, searching on google!")
            return "Unable to summarize, source not found, searching on google!"
    
    elif text.startswith("search on youtube"):
        returnVal = text.replace("search on youtube", "")
        pywhatkit.playonyt(returnVal)
        tts("Playing " + returnVal + " on youtube")
        return "Playing " + returnVal + " on youtube"
    
    elif text.startswith("open email"):
        returnVal = text.replace("open email", "")
        webbrowser.open("https://mail.google.com/mail/")

    else:
        try:
            response = ollama.generate(model="llama2", prompt="You are FOCUS (Friend Optimized For Comprehensive User Support)., Respond to the following text in no more than 45 lines" + text)
            tts(response["response"])
            return response["response"]
        except Exception:
            pass


@eel.expose
def draftEmail(text):
    prompt = text.replace("use header and footer", "") + "Do not start of with a generic response start, directly start with the content of the letter itself"
    email = ollama.generate(model="llama2", prompt=prompt)

    return email["response"]


    
eel.start('index.html')
