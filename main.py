import eel
import pyttsx3
import pywhatkit
import requests
import dotenv, os
import requests
from time import sleep
import wikipedia
import datetime

dotenv.load_dotenv()
api_key = os.getenv("llm_api_key")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": api_key}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	response = response.json()[0]
	response = response["generated_text"]
	answers = response.split("\n\n")
	return answers[1]

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

@eel.expose
def tts(text):

    engine.say(text)
    engine.runAndWait()
    engine.stop


@eel.expose 
def reqTimeOut(text):

    return round(len(text.split()) * (1/150))

@eel.expose
def greet():
     
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        tts("Good Morning!, always happy to assist")
    elif hour >= 12 and hour < 18:
        tts("Good Afternoon!, always happy to assist")
    else:
        tts("Good Evening!, always happy to assist")

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
            return query({"inputs": "You are FOCUS (Friend Optimized For Comprehensive User Support), Your job is to help the user with day to day desktop tasks, note that the user can be slurry and might make punctuation and spelling mistakes for example - 'hu r u' could be 'Who are you?' and 'what doin' could be 'what do you do?', assume the best case and respond, if you don't have any valid response - just say 'I am sorry, I can't help you with that question, it might be ambiguous....' Keeping this in mind, help the user with the following text whenever possible: " + text })
        except Exception:
             return "I am sorry, I wasn't able to get that"

def osActives(text):

    if "close browser" in text:
        os.system("taskkill /f /im firefox.exe")

@eel.expose
def timeout(time):
    sleep(time)

eel.init('frontend')
eel.start('index.html')