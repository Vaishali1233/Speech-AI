# YouTube Video Transcription, Translation, and Chatbot  

This project automates the process of **transcribing**, **translating**, and **chatbot interaction** with YouTube videos. Additionally, it converts the translated text into speech using **Text-to-Speech (TTS)**.

## Features  
**Download** YouTube audio  
**Transcribe** audio using OpenAI Whisper  
**Translate** transcript into a regional Indian language  
**Store embeddings** in FAISS for fast retrieval  
**Chatbot** to answer questions about the transcript  
**Convert text to speech (TTS)**  

---

### Install Dependencies  
pip install -r requirements.txt

---

## Technologies Used
**yt-dlp** → Download YouTube audio
**OpenAI Whisper** → Speech-to-text transcription
**FAISS** → Vector database for chatbot retrieval
**LangChain** → Chatbot implementation
**gTTS (Google Text-to-Speech)** → Convert text to speech
