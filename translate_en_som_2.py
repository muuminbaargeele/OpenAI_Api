from googletrans import Translator

def translate_somali_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src='so', dest='en')
    return translation.text

# Example usage:
somali_text = input('Enter Somali text to translate to English: ')
english_text = translate_somali_to_english(somali_text)
print(english_text)  # Outputs: Hello
