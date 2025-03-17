# Voice Assistant - Senpai CopyNinja

## 📌 Project Overview
Senpai CopyNinja is an AI-powered voice assistant that interacts with users through voice commands. It processes user queries based on predefined intents and responses stored in a structured JSON file. The assistant is built using **Natural Language Processing (NLP)** techniques and machine learning models trained to recognize various user inputs.

## 🚀 Features
- Speech recognition using `speech_recognition`
- Text-to-speech conversion using `pyttsx3`
- Custom intent recognition using `neuralintents`
- Interactive UI built with `tkinter`
- Real-time voice interaction
- Ability to activate (`start`) and deactivate (`stop`) via voice command
- Provides information about **Aniket Kumar**, including skills, projects, experience, and education
- Fallback mechanism for handling unrelated queries

## 📂 Project Structure
```
.voice-assistant/
│── .idea/
│── .gitignore
│── app.py            # Main application file
│── basic_model_intents.pkl
│── basic_model_words.pkl
│── basic_model.keras
│── dockerfile        # Docker configuration
│── intents.json      # Predefined intents and responses
│── LICENSE
│── main.py           # Core logic for assistant
│── newtest.py
│── README.md
│── requirements.txt  # Dependencies
│── test.py           # Testing scripts
```

## 📌 Technologies & Libraries Used
| Library            | Purpose |
|--------------------|---------|
| `speech_recognition` | Recognizes voice input |
| `pyttsx3`         | Converts text to speech |
| `neuralintents`   | Handles NLP-based intent recognition |
| `tkinter`         | GUI framework for visual interface |
| `threading`       | Manages concurrent execution |
| `sys`             | System-level operations |
| `json`            | Processes predefined intents |
| `pickle`          | Loads machine learning models |

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/aniketkumar8743/Voice-Assistant.git
cd Voice-Assistant
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```sh
python app.py
```

## 🐳 Running with Docker
### 1️⃣ Build the Docker Image
```sh
docker build -t voice-assistant .
```

### 2️⃣ Run the Docker Container
```sh
docker run -p 5000:5000 voice-assistant
```

## 🎯 How It Works
1. **Start Activation**: Saying "start" or "hello" turns on the assistant (green indicator).
2. **Listening Mode**: The assistant listens for user commands and matches them with predefined intents.
3. **Processing Input**: If the command is recognized, a response is generated and spoken aloud.
4. **Exit Command**: Saying "stop" turns off the assistant (black indicator) and closes the application.
5. **Fallback Response**: If an unknown question is asked, it returns a predefined response with Aniket Kumar’s contact details.

## 💡 Future Enhancements
- Integration with **LLaMA models** for improved NLP capabilities
- **Web API support** using FastAPI
- **RAG pipeline integration** for dynamic knowledge retrieval
- **Improved GUI** with more interactive elements

## 📧 Contact
For further information, feel free to reach out to **Aniket Kumar**:
📩 Email: [anikethkumar8743@gmail.com](mailto:anikethkumar8743@gmail.com)
🌐 GitHub: [https://github.com/aniketkumar8743](https://github.com/aniketkumar8743)

---
> **Note:** This project is under continuous development. Contributions and feedback are welcome!

