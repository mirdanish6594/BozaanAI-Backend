Bozaan.AI - Kashmiri Voice Assistant (Backend)
This repository contains the backend server for Bozaan.AI, a voice-first AI assistant designed for the Kashmiri language. The API is built with FastAPI and handles the entire end-to-end pipeline from receiving user audio to returning an AI-generated audio response.

This project was created by Danish Mir as a demonstration of building a full-stack, AI-powered regional language application.

✨ Features
Audio Processing: Accepts various audio formats (e.g., .m4a, .webm, .mp3) and standardizes them for processing.

Speech-to-Text: Utilizes OpenAI's Whisper model to transcribe spoken Kashmiri into text.

AI Response Generation: Leverages the OpenAI API (GPT-4o mini) to generate intelligent, conversational replies in Kashmiri.

Text-to-Speech: Converts the AI's text reply back into audible speech using gTTS.

Streaming Response: Efficiently streams the final audio back to the client for immediate playback.

🛠️ Tech Stack
Framework: FastAPI

Server: Uvicorn

Speech-to-Text: OpenAI Whisper

Language Model: OpenAI API (GPT-4o mini)

Text-to-Speech: gTTS (Google Text-to-Speech)

Audio Manipulation: pydub

🚀 Getting Started Locally
Follow these instructions to set up and run the backend server on your local machine.

Prerequisites
Python 3.9+

An OpenAI API Key

FFmpeg: This is a crucial system dependency for audio processing.

Windows: Download from gyan.dev and add the bin folder to your system's PATH.

macOS: brew install ffmpeg

Linux: sudo apt update && sudo apt install ffmpeg

Installation & Setup
Clone the repository:

git clone https://github.com/your-username/kashmiri-ai-backend.git
cd kashmiri-ai-backend

Create and activate a virtual environment:

# Create the environment
python -m venv venv

# Activate it
# On Windows (Git Bash)
source venv/Scripts/activate
# On macOS/Linux
source venv/bin/activate

Install the required packages:

pip install -r requirements.txt

Set up your environment variables:

Create a file named .env in the root directory.

Add your OpenAI API key to this file:

OPENAI_API_KEY="sk-proj-YourActualOpenAIKeyHere"

Run the server:

uvicorn main:app --reload

The server will be running at http://127.0.0.1:8000.

📡 API Endpoint
The server exposes a single primary endpoint for the voice assistant functionality.

Process User Audio
URL: /api/process-audio

Method: POST

Description: Receives an audio file, processes it through the entire STT -> LLM -> TTS pipeline, and streams the audio response back.

Request Body: multipart/form-data

audio: The audio file (.m4a, .webm, .mp3, .wav, etc.) recorded by the user.

Success Response:

Code: 200 OK

Content-Type: audio/mpeg

Body: The binary audio stream of the AI's reply.

Error Response:

Code: 500 Internal Server Error

Body: {"detail": "Error message"}

You can test this endpoint using the interactive documentation provided by FastAPI at http://127.0.0.1:8000/docs.

☁️ Deployment
This application is ready to be deployed on platforms like Render or Heroku.

Build Command: pip install -r requirements.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port 10000

Remember to set the OPENAI_API_KEY as an environment variable in your deployment service's settings.

```
📂 Project Structure
kashmiri-ai-backend/
├── api/
│   ├── __init__.py
│   └── main_router.py
├── services/
│   ├── __init__.py
│   ├── transcription_service.py
│   ├── llm_service.py
│   └── tts_service.py
├── .env
├── .gitignore
├── main.py
└── requirements.txt
```
