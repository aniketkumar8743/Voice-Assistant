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
        self.running = False  # Track active state

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
        self.label = tk.Label(text="🤖", font=("Arial", 180, "bold"))
        self.label.pack()

        threading.Thread(target=self.run_assistant, daemon=True).start()
        self.root.mainloop()

    def set_label_color(self, color):
        """Change the label color safely in the main thread"""
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

                    if "start" in text or "hello" in text:
                        print("✅ Assistant activated!")
                        self.running = True
                        self.set_label_color("green")
                        self.speak("Hi, I am Senpai CopyNinja, your voice assistant! How can I help you?")
                        continue  # Don't process an intent after activation

                    if "stop" in text:
                        print("🛑 Stopping Assistant...")
                        self.speak("Goodbye!")
                        self.set_label_color("black")  # Turn off light first
                        self.root.quit()
                        self.root.destroy()
                        sys.exit()

                    if self.running:
                        response = self.assistant.process_input(text)

                        # If the response is None or irrelevant, return a default message
                        if not response or response.lower() == "i don't know":
                            response = (
                                "Apologies, but I am still under development and not the appropriate source for this information. For further assistance, please contact Mr. Aniket Kumar at anikethkumar8743@gmail.com."
                            )

                        print(f"🤖 Bot response: {response}")
                        self.speak(response)

            except Exception as e:
                print(f"❌ Error: {e}")
                self.set_label_color("black")
                continue

    def speak(self, text):
        """Text-to-Speech with error handling"""
        try:
            print(f"🔊 Speaking: {text}")
            self.speaker.say(text)
            self.speaker.runAndWait()
        except Exception as e:
            print(f"❌ pyttsx3 error: {e}")


# ✅ Run the assistant
Assistant()
