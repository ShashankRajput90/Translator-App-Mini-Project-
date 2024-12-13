import whisper
from transformers import MarianMTModel, MarianTokenizer
from scipy.io.wavfile import write
import torch
from pydub import AudioSegment
from pydub.playback import play
import pyttsx3

class TranslatorWithCache:
    def __init__(self):
        self.model_cache = {}

    def get_translation_model(self, model_name):
        if model_name not in self.model_cache:
            tokenizer = MarianTokenizer.from_pretrained(model_name)
            model = MarianMTModel.from_pretrained(model_name)
            self.model_cache[model_name] = (tokenizer, model)
        return self.model_cache[model_name]

    def translate_text(self, text, target_lang):
        model_name = f"Helsinki-NLP/opus-mt-en-{target_lang}"
        tokenizer, model = self.get_translation_model(model_name)
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated_tokens = model.generate(**inputs)
        return tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    

class OfflineTranslator:
    def __init__(self):
        # Load Whisper for Speech-to-Text
        self.whisper_model = whisper.load_model("small")

        # Load MarianMT (offline translation model)
        self.translation_model_name = "Helsinki-NLP/opus-mt-en-ROMANCE"  # Translate English to Romance languages
        self.tokenizer = MarianTokenizer.from_pretrained(self.translation_model_name)
        self.translation_model = MarianMTModel.from_pretrained(self.translation_model_name)

        # Initialize Text-to-Speech engine (can replace with VITS for advanced TTS)
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty("rate", 150)

    def speech_to_text(self, audio_file):
        try:
            result = self.whisper_model.transcribe(audio_file)
            return result.get("text", "")
        except Exception as e:
            print(f"Error in speech-to-text: {e}")
            return ""

    def translate_text(self, text, target_lang):
        try:
            # Switch MarianMT model for specific language pair dynamically
            self.translation_model_name = f"Helsinki-NLP/opus-mt-en-{target_lang}"
            self.tokenizer = MarianTokenizer.from_pretrained(self.translation_model_name)
            self.translation_model = MarianMTModel.from_pretrained(self.translation_model_name)

            # Tokenize and translate
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
            translated_tokens = self.translation_model.generate(**inputs)
            translated_text = self.tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
            return translated_text
        except Exception as e:
            print(f"Error in text translation: {e}")
            return ""

    def text_to_speech(self, text, lang="en"):
        try:
            self.tts_engine.setProperty("voice", lang)
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"Error in text-to-speech: {e}")

    def speech_to_speech(self, audio_file, target_lang):
        text = self.speech_to_text(audio_file)
        translated_text = self.translate_text(text, target_lang)
        self.text_to_speech(translated_text, lang=target_lang)
