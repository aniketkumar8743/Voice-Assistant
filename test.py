import sys
import threading
import tkinter as tk
import speech_recognition as sr
import pyttsx3 as tts
from neuralintents import BasicAssistant

class Assistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)
        self.running = False  # Tracks if assistant is active

        print("🔊 Testing pyttsx3 speech...")
        self.speaker.say("Voice Assistant is starting!")
        self.speaker.runAndWait()

        try:
            self.assistant = BasicAssistant('intents.json')
            if self.assistant.model is None:
                print("🚨 Model not found! Training a new model...")
                self.assistant.fit_model()
                self.assistant.save_model()
                print("✅ Model trained and saved!")
            else:
                print("✅ Model loaded successfully!")
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            sys.exit(1)

        self.root = tk.Tk()
        self.root.title("Voice Assistant")
        self.label = tk.Label(text="🤖", font=("Arial", 120, "bold"))
        self.label.pack()

        threading.Thread(target=self.run_assistant, daemon=True).start()
        self.root.mainloop()

    def set_label_color(self, color):
        self.root.after(0, lambda: self.label.config(fg=color))

    def run_assistant(self):
        while True:
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=1.0)
                    print("🎤 Listening...")
                    audio = self.recognizer.listen(mic)
                    
                    try:
                        text = self.recognizer.recognize_google(audio).lower().strip()
                        print(f"👤 User said: {text}")
                    except sr.UnknownValueError:
                        print("⚠️ Could not understand the audio")
                        continue
                    except sr.RequestError:
                        print("⚠️ Speech recognition service is unavailable")
                        continue

                    if text in ["start", "hello"]:
                        print("✅ Assistant Activated!")
                        self.running = True  # Activate assistant
                        self.set_label_color("green")
                        self.speak("I am listening!")

                    if text == "stop":
                        print("🛑 Stopping Assistant...")
                        self.running = False  # Deactivate assistant
                        self.set_label_color("black")
                        self.speak("Goodbye!")
                        sys.exit()
                        
                    if self.running:
                        response = self.assistant.process_input(text)
                        if response:
                            print(f"🤖 Bot response: {response}")
                            self.speak(response)
            except Exception as e:
                print(f"❌ Error: {e}")
                continue

    def speak(self, text):
        try:
            print(f"🔊 Speaking: {text}")
            self.speaker.say(text)
            self.speaker.runAndWait()
        except Exception as e:
            print(f"❌ pyttsx3 error: {e}")

Assistant()
