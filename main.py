import eel
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import webbrowser
import ollama
import pyautogui
import subprocess


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
            result = wikipedia.summary(returnVal, sentences=3)
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
        tts(f"Playing {returnVal} on youtube")
        return f"Playing {returnVal} on youtube"
    
    elif text.startswith("open email"):
        returnVal = text.replace("open email", "")
        webbrowser.open("https://mail.google.com/mail/")

    else:
        try:
            response = ollama.generate(model="llama2", prompt="You are FOCUS (Friend Optimized For Comprehensive User Support)." + text)
            tts(response["response"])
            return response["response"]
        except Exception:
            pass

@eel.expose
def type(text):

    while text != "stop typing":

        if text == "copy text":
            pyautogui.hotkey("ctrl", "c")
        elif text == "cut text":
            pyautogui.hotkey("ctrl", "x")
        elif text == "paste text":
            pyautogui.hotkey("ctrl", "v")
        elif text == "undo change":
            pyautogui.hotkey("ctrl", "z")
        elif text == "redo change":
            pyautogui.hotkey("ctrl", "y")
        elif text == "save this":
            pyautogui.hotkey("ctrl", "s")
        elif text == "exit program":
            pyautogui.hotkey("alt", "f4")
        elif text == "select line":
            pyautogui.click(clicks=2, interval=0.25)
        elif text == "select all":
            pyautogui.hotkey("ctrl", "a")
        elif text == "find in this":
            pyautogui.hotkey("ctrl", "f")
        elif text == "replace this":
            pyautogui.hotkey("ctrl", "h")
        else:
            pyautogui.typewrite(text)
    
@eel.expose
def openApp(appName):

    if appName == "notepad":
        subprocess.Popen("notepad.exe")
    
eel.start('index.html')
