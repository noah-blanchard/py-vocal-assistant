import requests
import random
from speech_processing import SpeechProcessing

class TriviaAgent:
    def __init__(self):
        self.base_url = "https://the-trivia-api.com/v2/questions"
    
    def get_question(self):
        try:
            params = {
                "limit": 1
            }
            response = requests.get(self.base_url, params=params)

            if response.status_code == 200:
                data = response.json()[0]
                question_data ={
                    "category": data['category'],
                    "correct": data['correctAnswer'],
                    "incorrect": data['incorrectAnswers'],
                    "question": data["question"]["text"]
                }
                return question_data
        
        except Exception as e:
            print("There was an error.")