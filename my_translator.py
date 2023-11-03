from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def translate_text(subscription_key, service_region, source_language, target_language, text_to_translate):
    endpoint = f"https://{service_region}.api.cognitive.microsoft.com/"
    credential = AzureKeyCredential(subscription_key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

    documents = [text_to_translate]
    results = text_analytics_client.translate(documents, source_language=source_language, target_languages=[target_language])

    for result in results:
        translated_text = result.translations[0].text
        print(f"Original Text: {text_to_translate}")
        print(f"Translated Text: {translated_text}")

if __name__ == "_main_":
    subscription_key = 'a062ff7dd68d47aabcff0de395fa44b0'
    service_region = 'southafricanorth'
    source_language = 'so'  # Source language code, e.g., 'en' for English
    target_language = 'en'  # Target language code, e.g., 'fr' for French
    text_to_translate = """Annaga hadda waxaa ku faxasan nahay inaan bandhiggaan ka soo qaygalno. Maxaa yeelay waa aynu ka faa'ideysanaynaa barnaamijkaan sida ugu macqulsan ugunna hufan.
"""

    x = translate_text(subscription_key, service_region, source_language, target_language, text_to_translate)
    print(x)