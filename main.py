from speech_processing import SpeechProcessing
from command_processing import CommandProcessing
from openai_agent import OpenAIAgent
from todo_manager import TodoManager
from weather_agent import WeatherAgent

class MainApp:
    def __init__(self):
        self.speech_processor = SpeechProcessing()
        self.command_processor = CommandProcessing()
        self.openai_agent = OpenAIAgent()
        self.todo_manager = TodoManager()
        self.weather_agent = WeatherAgent()

    def run(self):

        while True:
            command = self.speech_processor.listen()
            if command != "":

                label = self.command_processor.handle_command(command)
                print(f"Label recognized by GPT: {label}")

                if label == "to-do list":
                    self.todo_manager.handle_command(command)
                elif label == "weather":
                    self.weather_agent.handle_command(command)
                else:
                    gpt_answer = self.openai_agent.get_response(command)
                    print(f"ChatGPT Answered: {gpt_answer}")
                    self.speech_processor.speak(gpt_answer)

if __name__ == "__main__":
    app = MainApp()
    app.run()