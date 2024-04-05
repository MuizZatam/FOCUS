import eel
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyautogui
import webbrowser
import ollama
import base64
from email.message import EmailMessage
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def gmail_send_message():
    # Code to send email using Gmail API
    pass

# Initialize Eel
eel.init('frontend')

# Initialize pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

tts_in_progress = False

@eel.expose
def tts(text):
    global tts_in_progress
    tts_in_progress = True
    engine.say(text)
    engine.runAndWait()
    tts_in_progress = False

@eel.expose
def tts_in_progress():
    global tts_in_progress
    return tts_in_progress

@eel.expose
def greet():
    hour = datetime.datetime.now().hour
    greeting = "Good Morning!, Always Happy To Assist" if 0 <= hour < 12 else "Good Afternoon!, Always Happy To Assist" if 12 <= hour < 18 else "Good Evening!, Always Happy To Assist"
    tts(greeting)
    return greeting

@eel.expose
def basicInfo(text):
    if text == "exit":
        return "exit"
    elif text.startswith("google"):
        returnVal = text.replace("google", "")
        try:
            result = wikipedia.summary(returnVal, sentences=3)
            pywhatkit.search(returnVal)
            return result
        except Exception:
            pywhatkit.search(returnVal)
            return "Unable to summarize, source not found!"
    elif text.startswith("search on youtube"):
        returnVal = text.replace("search on youtube", "")
        pywhatkit.playonyt(returnVal)
        return f"Playing {returnVal} on youtube"
    elif text.startswith("open email"):
        returnVal = text.replace("open email", "")
        webbrowser.open("https://mail.google.com/mail/")
    elif text.startswith("send test email"):
        gmail_send_message()
    else:
        try:
            response = ollama.generate(model="phi", prompt="You are FOCUS (Friend Optimized For Comprehensive User Support), Your job is to help the user with day to day desktop tasks, note that the user can be slurry and might make punctuation and spelling mistakes for example - 'hu r u' could be 'Who are you?' and 'what doin' could be 'what do you do?', assume the best case and respond, if you don't have any valid response - just say 'I am sorry, I can't help you with that question, it might be ambiguous....', also use plaintext in response, no markdown and no other formats, Keeping this in mind, if you recieve a greeting, just keep the greeting back very very short - Hi!, Don't describe yourself completely if asked to. Help the user with the following text whenever possible: " + text)
            return response["response"]
        except Exception:
            pass

@eel.expose
def type(text):
    # Code to handle typing commands
    pass

eel.start('index.html')