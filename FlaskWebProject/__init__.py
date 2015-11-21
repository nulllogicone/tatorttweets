#!/usr/local/bin/python2.7

from flask import Flask
import os
import FlaskWebProject


# TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
# STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

# app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder = STATIC_FOLDER) 


app = Flask(__name__) 
app.config.from_object('config')

import views
