import os

from flask_sqlalchemy import SQLAlchemy
from app import app, platform, flask, render_template


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
