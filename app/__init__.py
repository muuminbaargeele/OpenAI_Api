"""
    __init__.py file is used to bring our application together
    and tell python interpreter 'this is a package'

"""
from datetime import timedelta
from flask_cors import CORS

"""  
    Note: You must import all of your packages into here at the same time 
    Create all of your obj here 
"""

from flask import Flask

app = Flask(__name__)
CORS(app)

from app import public_views
from app import openai_api
from app import som_to_en
from app import mygoogletrans
from app import tts



""" Create your objects here... Then you can use it in very where in your app. That is cool"""

app.config["SECRET_KEY"] = "promptsom"
# app.permanent_session_lifetime = timedelta(minutes=2)
app.permanent_session_lifetime = timedelta(days=365)