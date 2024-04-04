import eel
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import os
import google.generativeai as genai
import pyautogui

# Initialize Eel
eel.init('frontend')

# Initialize pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Initialize generative model
api_key = os.getenv("llm_api_key")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')


@eel.expose
def tts(text):
    engine.say(text)
    engine.runAndWait()


@eel.expose
def greet():
    hour = datetime.datetime.now().hour
    greeting = "Good Morning!" if 0 <= hour < 12 else "Good Afternoon!" if 12 <= hour < 18 else "Good Evening!"
    tts(f"{greeting} always happy to assist")


@eel.expose
def basicInfo(text):
    if text == "exit":
        return "exit"

    if text.startswith("google"):
        returnVal = text.replace("google", "")
        try:
            result = wikipedia.summary(returnVal, sentences=3)
        except wikipedia.exceptions.PageError:
            return "Unable to summarize, source not found!"
        pywhatkit.search(returnVal)
        return result

    if text.startswith("search on youtube"):
        returnVal = text.replace("search on youtube", "")
        pywhatkit.playonyt(returnVal)
        return f"Playing {returnVal} on youtube"

    try:
        response = model.generate_content("You are FOCUS (Friend Optimized For Comprehensive User Support), Your job is to help the user with day to day desktop tasks, note that the user can be slurry and might make punctuation and spelling mistakes for example - 'hu r u' could be 'Who are you?' and 'what doin' could be 'what do you do?', assume the best case and respond, if you don't have any valid response - just say 'I am sorry, I can't help you with that question, it might be ambiguous....', also use plaintext in response, no markdown and no other formats, Keeping this in mind, help the user with the following text whenever possible: " + text)
        return response.text
    except Exception:
        return "I am sorry, I wasn't able to get that"


@eel.expose
def osActives(text):
    if "close browser" in text:
        os.system("taskkill /f /im firefox.exe")
    elif "open app notepad" in text:
        npath = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(npath)

@eel.expose
def type(text):

    if text == "stop typing":

        return

    elif text == "paste":

        pyautogui.hotkey("ctrl", "v")
        
    elif text == "save changes":

        pyautogui.hotkey("ctrl", "s")

    elif text == "select line":

        pyautogui.doubleClick()
        
    elif text == "select all lines":

        pyautogui.hotkey("ctrl", "a")

    elif text == "move up":

        pyautogui.press("up")

    elif text == "move down":

        pyautogui.press("down")

    else:

        pyautogui.typewrite(text)




eel.start('index.html')
