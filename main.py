import eel
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import os
import requests
import pyautogui
import webbrowser

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
headers = {"Authorization": api_key}
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


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
    if text == "exit":
        return "exit"

    elif text.startswith("google"):
        returnVal = text.replace("google", "")
        try:
            result = wikipedia.summary(returnVal, sentences=3)
            pywhatkit.search(returnVal)
            return result
        except wikipedia.exceptions.PageError:
            pywhatkit.search(returnVal)
            return "Unable to summarize, source not found!"
            
        

    elif text.startswith("search on youtube"):
        returnVal = text.replace("search on youtube", "")
        pywhatkit.playonyt(returnVal)
        return f"Playing {returnVal} on youtube"

    elif text.startswith("open email"):
        returnVal = text.replace("open email", "")
        webbrowser.Chrome("https://mail.google.com/mail/")
    

    else:   
        try:
            output = query({
	            "inputs": "You are FOCUS (Friend Optimized For Comprehensive User Support), Your job is to help the user with day to day desktop tasks, note that the user can be slurry and might make punctuation and spelling mistakes for example - 'hu r u' could be 'Who are you?' and 'what doin' could be 'what do you do?', assume the best case and respond, if you don't have any valid response - just say 'I am sorry, I can't help you with that question, it might be ambiguous....', also use plaintext in response, no markdown and no other formats, Keeping this in mind, help the user with the following text whenever possible: " + text
            })
            output = output[0]
            output = output.get("generated_text")
            output = output.split('\n\n')[1]
            return output
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
    elif text == "paste text":
        pyautogui.hotkey("ctrl", "v")
    elif text == "save changes":
        pyautogui.hotkey("ctrl", "s")
    elif text == "select all":
        pyautogui.hotkey("ctrl", "a")
    elif text == "move up":
        pyautogui.press("up")
    elif text == "move down":
        pyautogui.press("down")
    elif text == "delete":
        pyautogui.press("backspace")
    elif text == "quit program":
        pyautogui.hotkey("alt", "f4")
    elif text == "copy text":
        pyautogui.hotkey("ctrl", "c")
    elif text == "cut text":
        pyautogui.hotkey("ctrl", "x")
    

    else:
        # Batch multiple keystrokes together for faster typing
        for char in text:
            pyautogui.typewrite(char)





eel.start('index.html')
