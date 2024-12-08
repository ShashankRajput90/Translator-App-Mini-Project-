import whisper
from TTS.api import TTS
from transformers import MarianMTModel, MarianTokenizer

def speech_to_text_offline(audio_file):
    model = whisper.load_model("base")  # Load the "base" Whisper model
    result = model.transcribe(audio_file)
    print("Transcribed Text:", result["text"])
    return result["text"]

def text_to_speech_offline(text, lang="en"):
    # Initialize the TTS model
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
    tts.tts_to_file(text=text, file_path="output.wav")
    print("Speech saved as output.wav")

def translate_text_offline(input_text, src_lang="en", tgt_lang="fr"):
    model_name = f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    # Tokenize and translate
    tokenized_text = tokenizer.prepare_seq2seq_batch([input_text], return_tensors="pt")
    translated = model.generate(**tokenized_text)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    print("Translated Text:", translated_text)
    return translated_text

def main():
    print("Select an option:")
    print("1: Speech-to-Speech")
    print("2: Text-to-Text")
    choice = int(input("Enter choice: "))

    if choice == 1:
        audio_path = input("Enter path to audio file: ")
        source_text = speech_to_text_offline(audio_path)
        translated_text = translate_text_offline(source_text, src_lang="en", tgt_lang="es")  # English to Spanish
        text_to_speech_offline(translated_text, lang="es")
    elif choice == 2:
        source_text = input("Enter text to translate: ")
        translated_text = translate_text_offline(source_text, src_lang="en", tgt_lang="fr")  # English to French
        text_to_speech_offline(translated_text, lang="fr")
    else:
        print("Invalid choice")