import os
import platform
import flask

from os import environ
from flask import Flask, request, flash, url_for, render_template, redirect
from dotenv import load_dotenv
from markupsafe import escape

# Load env and database configurations
load_dotenv(".env")

# Flask app initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = "pharmacyapp"

# Load db variable for cli command database_init()
from configs.database import db

# Load router configurations and importer of controlers
import configs.route

from models.drug import DrugModel
from models.transaction import TransactionModel
from models.user import UserModel

@app.before_first_request
def create_table():
    db.create_all()

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
    from flask_sqlalchemy import SQLAlchemy
    from configs.database import db
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