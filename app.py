import os
import platform
import flask
import logging
import logging.config
import locale

from os import environ
from pathlib import Path
from flask import Flask, request, flash, url_for, render_template, redirect, jsonify, make_response
from markupsafe import escape
from dotenv import load_dotenv
from datetime import datetime
from webpack_boilerplate.config import setup_jinja2_ext


locale.setlocale(locale.LC_ALL, '')

# Load env and database configurations
load_dotenv(".env")

# Logger configuration to current date filename in logs folder
logging.basicConfig(filename="logs/" + datetime.today().strftime('%Y-%m-%d') + ".log", filemode="w", format="[%(asctime)s] %(levelname)s | %(name)s | %(threadName)s : %(message)s")

# Flask app initialization and webpack bolerplate configuration
BASE_DIR = Path(__file__).parent
app = Flask(__name__, static_folder="static", static_url_path="/static/") # static_folder="frontend/build"
app.config.update({
    'WEBPACK_LOADER': {
        'MANIFEST_FILE': BASE_DIR / "static/manifest.json", # BASE_DIR / "frontend/build/manifest.json"
    }
})
app.config['SECRET_KEY'] = "pharmacyapp"
setup_jinja2_ext(app)

# Load db variable for cli command database_init()
from configs.database import db

from services.common import Common

# Load router configurations and importer of controlers
import configs.route

# Database intialization when first run
@app.before_first_request
def create_table():
    import models
    db.create_all()


# Error page
@app.errorhandler(404)
def page_not_found(error):
    data = {
        "content": "404.jinja",
        "title": "404",
    }

    Common.setLogger('error', 'Not found.', [])

    return render_template('index.jinja', data=data, os=os), 404


# Webpack initialization
@app.cli.command("webpack_init")
def webpack_init():
    from cookiecutter.main import cookiecutter
    import webpack_boilerplate
    pkg_path = os.path.dirname(webpack_boilerplate.__file__)
    cookiecutter(pkg_path, directory = "frontend_template")


# Database migration for initialization
@app.cli.command("database_init")
def database_init():
    #from flask_sqlalchemy import SQLAlchemy
    #from configs.database import db
    import models
    db.create_all()


########################## Experiment ##########################


@app.route("/hello", methods=['GET'])
def hello_world():
    greeting = "Hello world!"
    data = {
        "greeting": greeting,
    }

    return render_template('hello-world.jinja', data = data)


if __name__ == "__main__":
    app.run(debug=True)