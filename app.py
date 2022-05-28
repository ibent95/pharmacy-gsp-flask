import os
import platform
import flask
from flask import Flask
from flask import render_template
from markupsafe import escape
from gsp import GSP

# Flask
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

    transactions = [
        ["a", "b", "c", frozenset(["c", "d"]), "d"],
        ["a", "a", "b", frozenset(["c", "d"]), 'c'],
        ["a", "a"]
    ]

    alg = GSP(transactions=transactions, minsup=0.5)
    print(alg.run_alg()[-2])

    return render_template('index.jinja', data = data, os = os)

@app.route("/drug")
def drug():
    title = "Wellcome to my first project to learn Flask in Python."
    pythonSystemVersion = platform.python_version()
    flaskAppVersion = flask.__version__
    data = {
        "content": "drug/main.jinja",
        "title": title,
        "python_system_version": pythonSystemVersion,
        "flask_app_version": flaskAppVersion,
    }

    return render_template('index.jinja', data = data, os = os)

@app.route("/transaction")
def transaction():
    title = "Wellcome to my first project to learn Flask in Python."
    pythonSystemVersion = platform.python_version()
    flaskAppVersion = flask.__version__
    data = {
        "content": "drug/main.jinja",
        "title": title,
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

    return render_template('hello-world.jinja', data = data)

# Webpack initialization
@app.cli.command("webpack_init")
def webpack_init():
    from cookiecutter.main import cookiecutter
    import webpack_boilerplate
    pkg_path = os.path.dirname(webpack_boilerplate.__file__)
    cookiecutter(pkg_path, directory = "frontend_template")