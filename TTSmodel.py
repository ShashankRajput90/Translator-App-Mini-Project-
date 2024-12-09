import whisper
model = whisper.load_model("small")
result = model.transcribe("sample_audio.wav")
print("Transcribed Text:", result["text"])
