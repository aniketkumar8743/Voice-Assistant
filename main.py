import sys         # allows you to interact with the Python runtime environment, including handling input/output
import threading
import tkinter as tk        # Create a GUI for User Interaction
import speech_recognition    # Convert speech to text
import pyttsx3 as tts        # Convert text to speech
from neuralintents import BasicAssistant # Neural Network Create an intent-based AI Chatbot

class Assistant:
  def __init__(self):
    self.recognizer = speech_recognition.Recognizer()  # Create a speech recognizer
    self.speaker = tts.init()  #  Create a text-to-speech engine
    self.speaker.setProperty("rate", 150) # Set the speech rate
    
    self.assistant = BasicAssistant('intents.json') # Create an intent-based AI Chatbot
    #self.assistant.train() # Train the intent-based AI Chatbot
    
    self.root = tk.Tk() # Create a tkinter window
    self.label = tk.Label(text="🤖",font=("Airal",120,"bold")) # icon and style
    self.label.pack() # Pack the label into the tkinter window
    
    threading.Thread(target=self.run_assistant).start() # Start a new thread to run the assistant
    
    self.root.mainloop()
    
    
  def create_file(self):
    with open("ani.txt",'w') as f:
      f.write("Created by Me")
    
  def run_assistant(self):
    while True:
      try:
        with speech_recognition.Microphone() as mic: # Create a speech recognizer
          self.recognizer.adjust_for_ambient_noise(mic, duration=0.2) # Adjust for ambient noise
          audio = self.recognizer.listen(mic) # Listen for speech
            
          text = self.recognizer.recognize_google(audio) # Convert speech to text
          text = text.lower() # Convert text to lowercase
            
          if "Hello A" in text:
            self.label.config(fg="green") # Change the label color to green
            audio = self.recognizer.listen(mic) # Listen for speech
            text = self.recognizer.recognize_google(audio) # Convert speech to text
            text = text.lower() # Convert text to lowercase
            if text == "stop":
              self.speaker.say("Goodbye!") # Say goodbye
              self.speaker.runAndWait() # Run the text-to-speech engine
              self.speaker.stop() # Stop the text-to-speech engine
              self.root.destroy() # Destroy the tkinter window
              sys.exit() # Exit the program
            else:
              if text is not None:
                response = self.assistant.request(text) # Get the response from the intent-based AI Chatbot
                if response is not None:
                  self.speaker.say(response) # Say the response
                  self.speaker.runAndWait() # Run the text-to-speech engine
              self.label.config(fg="black") # Change the label color to black
      except:
        self.label.config(fg="black") # Change the label color to black
        continue   
               
Assistant() 