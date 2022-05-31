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

@app.route("/generalized-sequential-pattern-calculation-result", methods=['GET'])
def generalized_sequential_pattern_calculation_result():
    title = "Hasil perhitungan Generalized Sequential Pattern (GSP)"
    #transactions = [
    #    ["a", "b", "c", frozenset(["c", "d"]), "d"],
    #    ["a", "a", "b", frozenset(["c", "d"]), 'c'],
    #    ["a", "a"]
    #]

    transactions = [
        [
            frozenset({'sv'}), frozenset({'x'}), frozenset({'+', 'qo', 'sv'}), frozenset({'sv'}), frozenset({'x'}), frozenset({'sd', 'sv'}), frozenset({'%', 'sd', 'sv'}), frozenset({'b'}), frozenset({'+', 'sd'}), frozenset({'sv'}), frozenset({'+'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'%', 'aa'}), frozenset({'+', 'sv'}), frozenset({'b'}), frozenset({'sv'}), frozenset({'b'}), frozenset({'+', 'sv(^q)'}), frozenset({'aa'}), frozenset({'+', '^q', 'qh'}), frozenset({'aa'}), frozenset({'sv'}), frozenset({'sv'}), frozenset({'+', 'sv'}), frozenset({'%', 'sd', 'sv', 'sv^r'}), frozenset({'^q', 'qh', 'sd', 'sv', 'sv(^q)'}), frozenset({'aa'}), frozenset({'+'}), frozenset({'aa', 'sv'}), frozenset({'sd'}), frozenset({'bf'}), frozenset({'aa', 'sd'}), frozenset({'b^m'}), frozenset({'+'}), frozenset({'b'}), frozenset({'%', 'o', 'qy'}), frozenset({'qr'}), frozenset({'b', 'sd'}), frozenset({'%'}), frozenset({'+'}), frozenset({'x'}), frozenset({'+', 'sd'}), frozenset({'^2'}), frozenset({'sd'}), frozenset({'%'}), frozenset({'+', 'sd'}), frozenset({'b'}), frozenset({'+'}), frozenset({'aa', 'sd', 'sv'}), frozenset({'aa', 'sd'}), frozenset({'b'}), frozenset({'^q', 'sd(^q)'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'b', 'qw'}), frozenset({'sd'}), frozenset({'b', 'ba'}), frozenset({'aa', 'sd^t'}), frozenset({'x'}), frozenset({'+'}), frozenset({'x'}), frozenset({'+'}), frozenset({'b'}), frozenset({'+', 'sd^t'}), frozenset({'b'}), frozenset({'sd^t'}), frozenset({'bk'})
        ],
        [
            frozenset({'sd', 'sd^t'}), frozenset({'ba'}), frozenset({'b', 'sd^t'}), frozenset({'ba'}), frozenset({'sv^t'}), frozenset({'aa'}), frozenset({'ad'}), frozenset({'^h', 'aa'}), frozenset({'x'}), frozenset({'sd'}), frozenset({'aa', 'sv'}), frozenset({'sd'}), frozenset({'+'}), frozenset({'aa', 'sd'}), frozenset({'%'}), frozenset({'^h', 'sd'}), frozenset({'aa'}), frozenset({'+', '^h', 'sd', 't1'}), frozenset({'b'}), frozenset({'%'}), frozenset({'qy'}), frozenset({'sd'}), frozenset({'b', 'bf'}), frozenset({'qw', 'sd'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'b', 'b^r', 'sd'}), frozenset({'x'}), frozenset({'+'}), frozenset({'b'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'sv'}), frozenset({'sd'}), frozenset({'sv'}), frozenset({'+'}), frozenset({'b', 'sd'}), frozenset({'sd'}), frozenset({'aa', 'aa^r', 'sv'}), frozenset({'sv'}), frozenset({'b', 'b^r'}), frozenset({'%', 'sd'}), frozenset({'ba', 'sv'}), frozenset({'%', 'b'}), frozenset({'%', 'qy'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'sd'}), frozenset({'sv'}), frozenset({'ba'}), frozenset({'+'}), frozenset({'qw'}), frozenset({'sd'}), frozenset({'%', 'b^m', 'bk', 'sd'}), frozenset({'b'}), frozenset({'%', '+'}), frozenset({'ad', 'b'}), frozenset({'aa', 'sd'}), frozenset({'sd', 'sv'}), frozenset({'+'}), frozenset({'+'}), frozenset({'b', 'b^r'}), frozenset({'sd'}), frozenset({'%', 'qy'}), frozenset({'%', 'sd'}), frozenset({'b', 'b^r', 'qo', 'sd'}), frozenset({'sd'}), frozenset({'%'}), frozenset({'sd', 'sv'}), frozenset({'%'}), frozenset({'sv'}), frozenset({'sd'}), frozenset({'sd'}), frozenset({'b', 'b^r'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'sd'}), frozenset({'b', 'b^r'}), frozenset({'sd'}), frozenset({'sd'}), frozenset({'%'}), frozenset({'+', 'sd'}), frozenset({'b'}), frozenset({'+'}), frozenset({'b', 'sd'}), frozenset({'+'}), frozenset({'qy'}), frozenset({'+'}), frozenset({'+'}), frozenset({'sd'}), frozenset({'bh'}), frozenset({'sd'}), frozenset({'b', 'b^r'}), frozenset({'%', '+'}), frozenset({'b', 'qy^g'}), frozenset({'ny', 'ny^r'}), frozenset({'sv'}), frozenset({'qh', 'sv'}), frozenset({'aa', 'sv'}), frozenset({'%', 'b', 'b^r'}), frozenset({'sv'}), frozenset({'aa'}), frozenset({'sd'}), frozenset({'%', 'aa', 'sd'}), frozenset({'sv'}), frozenset({'aa'}), frozenset({'sv'}), frozenset({'sd'}), frozenset({'aa', 'qh', 'sv'}), frozenset({'aa'}), frozenset({'+'}), frozenset({'sd(^q)'}), frozenset({'+'}), frozenset({'+'}), frozenset({'%'}), frozenset({'sd'}), frozenset({'aa', 'sd', 'sv'}), frozenset({'b'}), frozenset({'+'}), frozenset({'ba'}), frozenset({'sd'}), frozenset({'x'}), frozenset({'%', 'sd'}), frozenset({'fe', 'qy'}), frozenset({'sd'}), frozenset({'%', '+'}), frozenset({'nn', 'sd^e'}), frozenset({'%', 'sd', 'x'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'sd', 'sv'}), frozenset({'aa', 'sd'})
        ],
        [
            frozenset({'o', 'qrr', 'qw', 'sd', 'sv'}), frozenset({'sd'}), frozenset({'b'}), frozenset({'+'}), frozenset({'aa'}), frozenset({'sd'}), frozenset({'b', 'sd'}), frozenset({'b'}), frozenset({'sd', 'sd(^q)'}), frozenset({'x'}), frozenset({'%', 'sd'}), frozenset({'sv'}), frozenset({'aa', 'sd'}), frozenset({'b'}), frozenset({'h', 'sd'})
        ]
    ]

    minSupport = 0.2

    alg = GSP(transactions = transactions, minsup = minSupport)
    result = alg.run_alg()
    print(result)

    data = {
        "content": "generalized-sequential-pattern.jinja",
        "title": title,
        "transactions": transactions,
        "minimal_support": minSupport,
        "result": result
    }

    return render_template('index.jinja', data = data, os = os)


# Sign in and sign out
@app.route("/signin", methods=['GET'])
def signin_form():
    data = {
        "content": "authentication/sign-in.jinja",
    }

    return render_template('authentication.jinja', data = data, os = os)

@app.route("/signin", methods=['POST'])
def signin():
    data = {
        "content": "authentication/sign-in.jinja",
    }

    return render_template('authentication.jinja', data = data, os = os)

@app.route("/signout", methods=['POST'])
def signout():
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