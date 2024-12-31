# Translator App

# Offline Language Translator with Speech and Text Capabilities

## 🌟 Overview
This is a Python-based **Offline Language Translator** with a user-friendly GUI that supports:
- **Speech-to-Text**: Converts spoken language from an audio file into text.
- **Text-to-Text Translation**: Translates text from one language to another.
- **Speech-to-Speech Translation**: Translates spoken input into another language and outputs the translated speech.

The app is built using state-of-the-art Machine Learning models and frameworks, making it efficient and entirely offline.

---

## ✨ Features
1. **Speech Recognition**:
   - Converts audio files into text.
   - Supports multiple languages for input.

2. **Text Translation**:
   - Translates text between various languages.
   - Uses pre-trained machine translation models for accuracy.

3. **Text-to-Speech**:
   - Converts translated text into speech.
   - Supports different accents and voices for multiple languages.

4. **Graphical User Interface (GUI)**:
   - Simple and intuitive interface for ease of use.
   - Options to select input/output languages and upload audio files.

---

# ✨ Required Dependencies

   ### Core Dependencies
   - **torch**: For running PyTorch-based models used by transformers.
   - **whisper**: For speech-to-text functionality using OpenAI's Whisper model.
   - **transformers**: For working with pre-trained translation models like MarianMT.
   - **VITS (via pip or a repository)**: For speech synthesis.
   - **tkinter**: For the graphical user interface (GUI).
   - **pygame**: For managing sounds, fonts, and other media in GUI.

   ### Utility Dependencies
   - **pyttsx3**: For text-to-speech synthesis.
   - **speechrecognition**: For converting speech to text.
   - **pyaudio**: For capturing microphone input (required by speechrecognition).
   - **numpy**: A helper library often required for scientific computation.
   - **scipy**: Useful in some cases for advanced processing.

   ### Optional Dependencies
   - **requests**: For any online API calls.
   - **pillow**: For image processing in GUI if necessary.

---
## 🛠️ Technologies Used
- **Python**: Programming language.
- **Whisper**: For offline speech-to-text conversion.
- **Transformers (Hugging Face)**: For language translation.
- **TTS (Text-to-Speech)**: For generating speech from text.
- **Tkinter**: For the graphical user interface.

---

## 🎯 How It Works
1. **Select an Operation**:
   - Speech-to-Speech
   - Text-to-Text

2. **Provide Input**:
   - Upload an audio file or enter text.

3. **Select Languages**:
   - Choose the source and target languages.

4. **Get Results**:
   - View translated text or listen to the output audio.

---

## 🖥️ Screenshots

### Main Interface
![Screenshot 2024-12-31 194923](https://github.com/user-attachments/assets/9fda7fbd-7abc-481e-9357-4ab50c777ef0)


### Translation in Action
![Screenshot 2024-12-31 195221](https://github.com/user-attachments/assets/3dac4000-77ab-4a4c-bab8-47a0a230fe39)


---

## 🚀 Setup and Usage

### Prerequisites
- Python 3.8 or higher
- Install the required libraries:
  ```bash
   pip install transformers torch whisper
   pip install tkinter pygame
   pip install pyttsx3 speechrecognition pyaudio
   pip install numpy scipy pillow requests

   


