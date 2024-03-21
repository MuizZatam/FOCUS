import eel
import pyttsx3
import pywhatkit
import requests
import dotenv, os
import requests
from time import sleep

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
engine.setProperty('rate', 135)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

@eel.expose
def tts(text):

    engine.say(text)
    engine.runAndWait()
    engine.stop

@eel.expose
def basicInfo(text):
    
    if text == "exit":
        return "exit"
    
    elif str(text).find("google") == 0:
        returnVal = str(text).replace("google", "")
        pywhatkit.search(returnVal)
        return f"Searching for {returnVal} on Google"     
      
    elif str(text).find("search on youtube") == 0:
        returnVal = str(text).replace("search on youtube", "")
        pywhatkit.playonyt(returnVal)
        return f"Playing {returnVal} on youtube"
        
    else:
        try:
            return query({"inputs": "You are FOCUS (Friend Optimized For Comprehensive User Support), Your job is to help the user with day to day desktop tasks, note that the user can be slurry and might make punctuation and spelling mistakes for example - 'hu r u' could be 'Who are you?' and 'what doin' could be 'what do you do?', assume the best case and respond, if you don't have any valid response - just say 'I am sorry, I can't help you with that question, it might be ambiguous....' Keeping this in mind, help the user with the following text whenever possible: " + text })
        except Exception:
             return "I am sorry, I wasn't able to get that"

@eel.expose
def timeout():
     sleep(5)

eel.init('frontend')
eel.start('index.html')