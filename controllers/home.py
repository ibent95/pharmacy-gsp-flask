import os

from flask_sqlalchemy import SQLAlchemy
from app import app, request, platform, flask, render_template
from services.gsp import GSP


# Home
@app.route("/", methods=['GET'])
def index():
    title = "Ikhtisar"
    greeting = "Wellcome to my first project to learn Flask in Python."
    pythonSystemVersion = platform.python_version()
    flaskAppVersion = flask.__version__
    data = {
        "content": "home.jinja",
        "title": title,
        "greeting": greeting,
        "python_system_version": pythonSystemVersion,
        "flask_app_version": flaskAppVersion,
    }

    return render_template('index.jinja', data = data, os = os)