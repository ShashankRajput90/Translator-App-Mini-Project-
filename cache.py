from transformers import MarianMTModel, MarianTokenizer

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
