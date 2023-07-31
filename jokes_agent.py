import requests
from speech_processing import SpeechProcessing
import os
from dotenv import load_dotenv

load_dotenv()

class JokesAgent:
    def __init__(self):
        self.base_url = "https://api.api-ninjas.com/v1/jokes"
        self.speech_processor = SpeechProcessing()
        self.api_key = os.getenv("APININJA_API_KEY")
    
    def handle_command(self, command):
        self.speech_processor.speak("I always have a good joke to tell ! Let me search inside of my machine brain...")
        self.tell_joke()

    def tell_joke(self):
        joke = self.get_joke()
        self.speech_processor.speak("Okay, here's a joke :", rephrase=False)
        self.speech_processor.speak(joke, rephrase=False)
    

    def get_joke(self, limit=1):
        try:
            params = {
                "limit": limit
            }

            headers = {
                "X-Api-Key": self.api_key
            }

            response = requests.get(self.base_url, params=params, headers=headers)

            if response.status_code == 200:
                joke = response.json()[0]["joke"]
                return joke
            else:
                self.speech_processor.speak("Sorry... I wasn't able to find any good jokes...")
            
        except Exception as e:
            print("There was an error accessing the jokes api : ", e)
            self.speech_processor.speak("Sorry... I wasn't able to find any good jokes...")
        
        return None