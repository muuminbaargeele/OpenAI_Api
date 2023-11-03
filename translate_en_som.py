from translate import Translator


# Function to translate English to Somali

def translate_english_to_somali(text):
    try:
        translator = Translator(to_lang="so")
        translation = translator.translate(text)
        return translation
    except Exception as e:
        return str(e)

# Example usage:
english_text = input('Enter English text to translate to Somali: ')
somali_translation = translate_english_to_somali(english_text)
print(somali_translation)