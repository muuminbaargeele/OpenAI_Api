x = 'AIzaSyD5daUsBbTzk06t8JORfBstaQR9IkydAhg'
import os
# import google cloud translate
from google.cloud import translate_v2 as translate
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"


def translate_english_to_somali(text):
    try:
        translator = translate.Client()
        translation = translator.translate(text, source_language='en', target_language='so')
        return translation['input']
    except Exception as e:
        return str(e)

# Example usage:
english_text = "Hello, how are you?"
somali_translation = translate_english_to_somali(english_text)
print(somali_translation)

