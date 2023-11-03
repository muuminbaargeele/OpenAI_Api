import openai
import time
from app.mygoogletrans import translate_text
from app.tts import SpeakMyWords



# Set your API key

api_key = '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'
# Initialize an empty conversation
conversation = []

# Initialize the OpenAI client
openai.api_key = api_key

def chat_with_ai(user_question):
    try:
        som_to_en = translate_text(user_question,"so","en")
        # Add the user's question to the conversation
        conversation.append({"role": "user", "content": som_to_en})

        # Generate a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use a different model
            messages=conversation
        )

        # Get the assistant's reply
        assistant_reply = response['choices'][0]['message']['content']

        # Add the assistant's reply to the conversation
        conversation.append({"role": "assistant", "content": assistant_reply})

        return assistant_reply

    except openai.error.OpenAIError as e:
        # Handle API errors
        return f"OpenAI API Error: {e}"
    except Exception as e:
        # Handle other unexpected errors
        return f"An error occurred: {e}"

def print_typewriter(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)  # Adjust the sleep time for your desired typing speed
    print()  # Add a newline after the typewriter effect


if __name__ == "__main__":

    # Example usage:
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat_with_ai(user_input)
        print("Assistant:", end=' ')
        en_to_som = translate_text(response, "en", "so")
        print_typewriter(en_to_som)
        speak = SpeakMyWords()
        speak.cong_words(en_to_som)
#
#     x = """
#     Aniga ma awoodo inaan adeeg ka gato Google. Galabtana waxaan leeyahay wax-soo-jeedin,. Ila tali maxaan samaynayaa?
#     """


