from googletrans import Translator

def translate_text(text, source_lang, target_lang):
    try:
        translator = Translator()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        return translated_text.text
    except Exception as e:
        return f"Translation error: {str(e)}"

def main():
    input_text = input("Enter the text you want to translate: ")
    source_lang = input("Enter the source language code (e.g., 'so' for Somali): ")
    target_lang = input("Enter the target language code (e.g., 'en' for English): ")

    translated_text = translate_text(input_text, source_lang, target_lang)

    if not translated_text.startswith("Translation error"):
        print(f"Translated text: {translated_text}")
    else:
        print(translated_text)

if __name__ == "__main__":
    main()


# my_text = """Waxaa maanta iigu guntanaa inaan maalinta jimcaha lahaa bandhig. Bandhiggu waxa uu ku saabsabaa barnaamij oo maskaxda macmalka ah.
# Innaga oo koox ah ayaa waxaa naloo dhiibay mashruuc yar oo aan ku soo bandhigi doonno Masraxa Astaan.
# Maalinta koowaad, kooxdeenna mashruuca in baan ka samaynay oo waan qabanay fikraddii loo baahnaa ee uu mashruucu ku dhisnaa.
# Hase yeeshe ee waxaanu u baahanay inaan sii hufino oo aan ka dhigno mid ilaa xad sax ah oo lagu kalsoonaan karo isla markaana qadaadkiisu aad u yaryhiin."""
#


