import os
import platform
import flask

from os import environ
from flask import Flask
from flask import render_template
from dotenv import load_dotenv
from markupsafe import escape

# Load env and database configurations
load_dotenv(".env")

# Flask
app = Flask(__name__)

from configs.database import db
import configs.route

from models.drug import DrugModel
from models.transaction import TransactionModel

drugModel = DrugModel('AA1', 'A')
transactionModel = TransactionModel('A1', 'B')


# Webpack initialization
@app.cli.command("webpack_init")
def webpack_init():
    from cookiecutter.main import cookiecutter
    import webpack_boilerplate
    pkg_path = os.path.dirname(webpack_boilerplate.__file__)
    cookiecutter(pkg_path, directory = "frontend_template")

@app.cli.command("database_init")
def database_init():
    from flask_sqlalchemy import SQLAlchemy
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