from deep_translator import GoogleTranslator

def translate_to_marathi():
    # Take input from the user
    english_text = input("Enter text in English: ")

    # Translate the text to Marathi
    try:
        translation = GoogleTranslator(source='en', target='mr').translate(english_text)
        # Print the translated text
        print("Translated text in Marathi:", translation)
    except Exception as e:
        print("An error occurred:", e)

# Run the translation function
translate_to_marathi()
