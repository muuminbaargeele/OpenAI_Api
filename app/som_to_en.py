import requests
import uuid
import json

def translate_text_to_english(text, from_language, to_language):
    endpoint = "https://api.cognitive.microsofttranslator.com/"
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': from_language,
        'to': [to_language]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': 'a062ff7dd68d47aabcff0de395fa44b0',
        'Ocp-Apim-Subscription-Region': 'southafricanorth',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': text}]

    try:
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        response = request.json()
        translated_text = response[0]['translations'][0]['text']
        return translated_text
    except Exception as e:
        return str(e)

# Example usage:
subscription_key = "a062ff7dd68d47aabcff0de395fa44b0"
location = "southafricanorth"
text_to_translate = "Annaga hadda waxaa ku faxasan nahay inaan bandhiggaan ka soo qaygalno. Maxaa yeelay waa aynu ka faa'ideysanaynaa barnaamijkaan sida ugu macqulsan ugunna hufan."


if __name__ == "__main__":

    while True:
        text_to_translate = input('Enter Somali text to translate to English: ')
        if text_to_translate == 'quit':
            break
        translated_text = translate_text_to_english(text_to_translate, 'so', 'en')
        print(translated_text)

