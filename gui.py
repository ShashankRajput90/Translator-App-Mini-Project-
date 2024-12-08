import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from functools import partial
import os

# Import your offline translation modules
from your_translation_module import speech_to_text_offline, translate_text_offline, text_to_speech_offline

def process_speech_to_speech():
    audio_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("Audio Files", "*.wav *.mp3")])
    if not audio_path:
        return
    try:
        # Speech to Text
        source_text = speech_to_text_offline(audio_path)
        source_lang = source_lang_var.get()
        target_lang = target_lang_var.get()

        # Translate
        translated_text = translate_text_offline(source_text, src_lang=source_lang, tgt_lang=target_lang)
        translated_text_var.set(translated_text)

        # Text to Speech
        text_to_speech_offline(translated_text, lang=target_lang)
        messagebox.showinfo("Success", "Translation completed and saved as audio!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def process_text_to_text():
    source_text = text_input.get("1.0", tk.END).strip()
    if not source_text:
        messagebox.showerror("Error", "Please enter text to translate.")
        return
    try:
        source_lang = source_lang_var.get()
        target_lang = target_lang_var.get()

        # Translate
        translated_text = translate_text_offline(source_text, src_lang=source_lang, tgt_lang=target_lang)
        translated_text_var.set(translated_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def play_output_audio():
    if os.path.exists("output.wav"):
        os.system("start output.wav")  # Use 'open' for Mac or 'xdg-open' for Linux
    else:
        messagebox.showerror("Error", "No audio file found. Please perform a translation first.")

# Create the main application window
root = tk.Tk()
root.title("Offline Language Translator")

# Language Selection
source_lang_var = tk.StringVar(value="en")
target_lang_var = tk.StringVar(value="fr")

tk.Label(root, text="Source Language:").grid(row=0, column=0, padx=10, pady=5)
source_lang_dropdown = ttk.Combobox(root, textvariable=source_lang_var, values=["en", "es", "fr", "de", "hi"])
source_lang_dropdown.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Target Language:").grid(row=1, column=0, padx=10, pady=5)
target_lang_dropdown = ttk.Combobox(root, textvariable=target_lang_var, values=["en", "es", "fr", "de", "hi"])
target_lang_dropdown.grid(row=1, column=1, padx=10, pady=5)

# Text Input for Text-to-Text Translation
tk.Label(root, text="Enter Text:").grid(row=2, column=0, padx=10, pady=5)
text_input = tk.Text(root, height=5, width=40)
text_input.grid(row=2, column=1, padx=10, pady=5)

# Buttons
speech_to_speech_btn = tk.Button(root, text="Speech-to-Speech", command=process_speech_to_speech)
speech_to_speech_btn.grid(row=3, column=0, padx=10, pady=10)

text_to_text_btn = tk.Button(root, text="Text-to-Text", command=process_text_to_text)
text_to_text_btn.grid(row=3, column=1, padx=10, pady=10)

# Translated Text Output
tk.Label(root, text="Translated Text:").grid(row=4, column=0, padx=10, pady=5)
translated_text_var = tk.StringVar()
translated_text_label = tk.Label(root, textvariable=translated_text_var, wraplength=300, justify="left")
translated_text_label.grid(row=4, column=1, padx=10, pady=5)

# Play Output Audio Button
play_audio_btn = tk.Button(root, text="Play Output Audio", command=play_output_audio)
play_audio_btn.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()
