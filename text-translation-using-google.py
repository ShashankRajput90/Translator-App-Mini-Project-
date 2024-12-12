from googletrans import Translator

def translate_text(input_text, target_language="fr"):  # Example: Translate to French
    translator = Translator()
    translated = translator.translate(input_text, dest=target_language)
    print("Translated Text:", translated.text)
    return translated.text