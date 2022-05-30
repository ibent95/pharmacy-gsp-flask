import os
import platform
import flask
from flask import Flask
from flask import render_template
from markupsafe import escape
from gsp import GSP

# Flask
app = Flask(__name__)


# Home
@app.route("/", methods=['GET'])
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


# Login and logout
@app.route("/login", methods=['GET'])
def login_form():
    data = {
        "content": "authentication/sign-in.jinja",
    }

    return render_template('authentication.jinja', data = data, os = os)

@app.route("/login", methods=['POST'])
def login():
    data = {
        "content": "authentication/sign-in.jinja",
    }

    return render_template('authentication.jinja', data = data, os = os)

@app.route("/logout", methods=['POST'])
def logout():
    data = {
        "content": "authentication/sign-in.jinja",
    }

    return render_template('authentication.jinja', data = data, os = os)


# Drug
@app.route("/drug", methods=['GET'])
def drug():
    title = "Obat"
    data = {
        "content": "drug/main.jinja",
        "title": title,
    }

    return render_template('index.jinja', data = data, os = os)

@app.route("/drug/create", methods=['GET', 'POST'])
@app.route("/drug/update", methods=['GET', 'PUT'])
def drug_form():
    title = "Formulir master data obat"
    data = {
        "content": "drug/form.jinja",
        "title": title,
    }

    return render_template('index.jinja', data=data, os=os)


# Transaction
@app.route("/transaction", methods=['GET'])
def transaction():
    title = "Transaksi"
    data = {
        "content": "transaction/main.jinja",
        "title": title,
    }

    return render_template('index.jinja', data = data, os = os)

@app.route("/transaction/create", methods=['GET', 'POST'])
@app.route("/transaction/update", methods=['GET', 'PUT'])
def transaction_form():
    title = "Formulir transaksi"
    drugs = [
        {
            "id": 1,
            "name": "Amlodipin",
            "option_text": "Amlodipin"
        },
        {
            "id": 2,
            "name": "Domperidone",
            "option_text": "Domperidone"
        },
        {
            "id": 3,
            "name": "Inj della",
            "option_text": "Inj della"
        },
        {
            "id": 4,
            "name": "Pcm",
            "option_text": "Pcm"
        },
    ]
    data = {
        "content": "transaction/form.jinja",
        "title": title,
        "drugs": drugs,
    }

    return render_template('index.jinja', data=data, os=os)


# Webpack initialization
@app.cli.command("webpack_init")
def webpack_init():
    from cookiecutter.main import cookiecutter
    import webpack_boilerplate
    pkg_path = os.path.dirname(webpack_boilerplate.__file__)
    cookiecutter(pkg_path, directory = "frontend_template")


########################## Experiment ##########################


@app.route("/hello", methods=['GET'])
def hello_world():
    greeting = "Hello world!"
    data = {
        "greeting": greeting,
    }

    return render_template('hello-world.jinja', data = data)