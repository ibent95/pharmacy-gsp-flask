import os

from flask_sqlalchemy import SQLAlchemy
from app import app, platform, flask, render_template
from gsp import GSP


# Transaction
@app.route("/transaction", methods=['GET'])
def transaction():
    title = "Transaksi"
    data = {
        "content": "transaction/main.jinja",
        "title": title,
    }

    return render_template('index.jinja', data=data, os=os)


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
