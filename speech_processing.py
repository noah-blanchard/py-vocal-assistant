import speech_recognition as sr
import pyttsx3 as tts

class SpeechProcessing:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts_engine = tts.init()

        self.tts_engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
        self.tts_engine.setProperty ("rate", 178)

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = None
            try:
                audio = self.recognizer.listen(source, timeout=5)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                
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
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def queue(self, text):
        self.tts_engine.say(text)

    def runAndWait(self):
        self.tts_engine.runAndWait()