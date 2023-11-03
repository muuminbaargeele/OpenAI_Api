from urllib.parse import unquote
from urllib.parse import quote
from flask import render_template, redirect, url_for, request, flash, session, request, make_response, jsonify
from app import app
from app.mygoogletrans import translate_text
from app.openai_api import chat_with_ai
from app.tts import SpeakMyWords
app.secret_key = 'albasrawie'


# @app.route('/')
# @app.route('/hoy')
# def index():
#     return render_template('my_index.html')


# respond the pront
@app.route('/respond', methods=['GET', 'POST'])
def respond():
    if request.method == 'POST':
        if request.is_json:
            req = request.get_json()
            print(req)
            print('Please wait while chatGPT responds')
            assistant_reply = chat_with_ai(req.get('topic'))
            print(assistant_reply)

            en_to_som = translate_text(assistant_reply, "en", "so")
            print(en_to_som)

            my_respond = {
                'message': en_to_som
            }

            res = make_response(jsonify(my_respond), 200)

            print('Waan celinay jawaab! Hambalyo.')
            return res
        else:
            my_respond = {
                'message': 'Data is not in json format!',
                'status': 'error'
            }
            res = make_response(jsonify(my_respond), 404)
            return res

    return jsonify({'message': 'Waxaan u malaynaynaa in boggani aanu ahayn kan aad rabtay!'})


@app.route('/speak', methods=['POST'])
def speak():
    if request.method == 'POST':

        if request.is_json:
            req = request.get_json()
            print(req)
            print('Please wait while we sound...')
            myspeak = SpeakMyWords()
            myspeak.cong_words(req.get('topic'))
            # SpeakMyWords(req.get('Caasimadda dalka Soomaaliya waa Muqdisho'))

            my_respond = {
                'message': 'Waan ku celinay jawaab! Hambalyo.'
            }

            res = make_response(jsonify(my_respond), 200)

            print('Waan celinay jawaab! Hambalyo.')
            return res
        else:
            my_respond = {
                'message': 'Data is not in json format!',
                'status': 'error'
            }
            res = make_response(jsonify(my_respond), 404)
            return res
