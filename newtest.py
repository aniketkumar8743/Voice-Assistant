import sys
import speech_recognition as sr
import pyttsx3 as tts
from neuralintents import BasicAssistant  # Ensure this library is installed

class Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)

        # ✅ Load intents.json with error handling
        try:
            self.assistant = BasicAssistant('intents.json')
            print("✅ Successfully loaded BasicAssistant")
        except Exception as e:
            print(f"❌ Error loading intents.json: {e}")
            sys.exit(1)  # Exit if intents cannot be loaded

        # ✅ Print available methods for debugging
        print("🔍 Available methods in BasicAssistant:")
        print(dir(self.assistant))  # ✅ Debugging step

        # ✅ Run a test response if a method is found
        test_text = "hello"
        if hasattr(self.assistant, "chat"):
            response = self.assistant.chat(test_text)
            print(f"🤖 Assistant Response: {response}")
        elif hasattr(self.assistant, "reply"):
            response = self.assistant.reply(test_text)
            print(f"🤖 Assistant Response: {response}")
        elif hasattr(self.assistant, "get_response"):
            response = self.assistant.get_response(test_text)
            print(f"🤖 Assistant Response: {response}")
        else:
            print("⚠️ No valid method found for text processing.")

# ✅ Run the assistant
Assistant()
🔍 Available methods in BasicAssistant:
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_predict_intent', '_prepare_intents_data', 'fit_model', 'hidden_layers', 'history', 'intents', 'intents_data', 'lemmatizer', 'load_model', 'method_mappings', 'model', 'model_name', 'process_input', 'save_model', 'training_data', 'words']
⚠️ No valid method found for text processing.