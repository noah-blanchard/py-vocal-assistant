import speech_recognition as sr
import pyttsx3 as tts
from openai_agent import OpenAIAgent
import time

class SpeechProcessing:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts_engine = tts.init()
        self.openai_agent = OpenAIAgent()

        self.tts_engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        self.tts_engine.setProperty("rate", 178)

    def listen_for_wakeword(self):
        wakeword = "hey assistant"
        print("Waiting for wake word...")

        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio)
                if text.lower() == wakeword:
                    print("Wake word detected.")
                    return True
                    
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Couldn't request results from the Google Speech Recognition service")
            except Exception as e:
                print(f"There was an error: {e}")
            
            return False
                    

    def listen(self, timeout=5):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = None
            try:
                audio = self.recognizer.listen(source, timeout)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                return ""
                
            text = ""

            try:
                print("Recognizing...")
                text = self.recognizer.recognize_google(audio)
                print(f"User said: {text}")
            except sr.UnknownValueError:
                print("Google Speech could not recognize audio")
            except sr.RequestError:
                print("Couldn't request results from the Google Speech Recognition service")
            except Exception:
                print("There was an error")
            
            return text

    def speak(self, text):
        self.queue(text)
        self.runAndWait()

    def queue(self, text):
        rephrased_text = self.openai_agent.rephrase(text)
        self.tts_engine.say(rephrased_text)

    def runAndWait(self):
        self.tts_engine.runAndWait()