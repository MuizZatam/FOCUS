import eel
import pyttsx3
import pywhatkit
import requests
import dotenv, os
import requests
from time import sleep
import wikipedia
import datetime
import google.generativeai as genai

dotenv.load_dotenv()
api_key = os.getenv("llm_api_key")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

@eel.expose
def tts(text):

    engine.say(text)
    engine.runAndWait()
    engine.stop()


@eel.expose 
def reqTimeOut(text):

    return round(len(text.split()) * (1/150))


     
@eel.expose
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        greeting = "Good Morning!, always happy to assist"
    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon!, always happy to assist"
    else:
        greeting = "Good Evening!, always happy to assist"
    return greeting


@eel.expose
def basicInfo(text):
    
    if text == "exit":
        return "exit"
    
    elif str(text).find("google") == 0:
        returnVal = str(text).replace("google", "")
        try:
            result = wikipedia.summary(returnVal, sentences=3)
        except wikipedia.exceptions.PageError:
            return "Unable to summarize, source not found!"
        pywhatkit.search(returnVal)
        return result     
      
    elif str(text).find("search on youtube") == 0:
        returnVal = str(text).replace("search on youtube", "")
        pywhatkit.playonyt(returnVal)
        return f"Playing {returnVal} on youtube"
        
    else:
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
def timeout(time):
    try:
        sleep(time)
    except TypeError:
        sleep(5)
    
eel.init('frontend')
eel.start('index.html')