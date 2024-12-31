import tkinter as tk
from tkinter import filedialog, ttk
from translator_backend_offline import OfflineTranslator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Offline Language Translator")
        self.root.geometry("650x600")
        self.translator = OfflineTranslator()

        # Input text area
        self.input_text_label = tk.Label(root, text="Input Text:")
        self.input_text_label.pack(pady=5)
        self.input_text_area = tk.Text(root, height=5, width=50)
        self.input_text_area.pack()

        # Language dropdown
        self.lang_label = tk.Label(root, text="Select Target Language:")
        self.lang_label.pack(pady=5)
        self.lang_var = tk.StringVar()
        self.language_dropdown = ttk.Combobox(
            root, textvariable=self.lang_var, values=["fr", "es", "de", "it", "pt"]
        )
        self.language_dropdown.pack()

        # Buttons
        self.translate_btn = tk.Button(
            root, text="Translate Text", command=self.translate_text
        )
        self.translate_btn.pack(pady=10)

        self.tts_btn = tk.Button(root, text="Text to Speech", command=self.text_to_speech)
        self.tts_btn.pack(pady=5)

        self.stt_btn = tk.Button(root, text="Load Audio for Speech-to-Text", command=self.speech_to_text)
        self.stt_btn.pack(pady=5)

        # Output text area
        self.output_text_label = tk.Label(root, text="Translated Text:")
        self.output_text_label.pack(pady=5)
        self.output_text_area = tk.Text(root, height=5, width=50, state="disabled")
        self.output_text_area.pack()

    def translate_text(self):
        input_text = self.input_text_area.get("1.0", tk.END).strip()
        target_lang = self.lang_var.get()

        if input_text and target_lang:
            translated_text = self.translator.translate_text(input_text, target_lang)
            self.output_text_area.config(state="normal")
            self.output_text_area.delete("1.0", tk.END)
            self.output_text_area.insert("1.0", translated_text)
            self.output_text_area.config(state="disabled")

    def text_to_speech(self):
        text = self.input_text_area.get("1.0", tk.END).strip()
        lang = self.lang_var.get()
        if text and lang:
            self.translator.text_to_speech(text, lang=lang)

    def speech_to_text(self):
        audio_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav *.mp3")])
        if audio_file:
            transcribed_text = self.translator.speech_to_text(audio_file)
            self.input_text_area.delete("1.0", tk.END)
            self.input_text_area.insert("1.0", transcribed_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()