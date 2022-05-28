import os
import platform
import flask
from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    greeting = "Wellcome to my first project to learn Flask in Python."
    pythonSystemVersion = platform.python_version()
    flaskAppVersion = flask.__version__
    data = {
        "content": "home.jinja",
        "greeting": greeting,
        "python_system_version": pythonSystemVersion,
        "flask_app_version": flaskAppVersion,
    }

    return render_template('index.jinja', data = data, os = os)

@app.route("/hello")
def hello_world():
    greeting = "Hello world!"
    data = {
        "greeting": greeting,
    }

    return render_template('hello-world.html', data = data, jinjaEnv = jinjaEnv)