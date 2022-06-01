import os

from flask_sqlalchemy import SQLAlchemy
from app import app, platform, flask, render_template


# Sign in and sign out
@app.route("/signin", methods=['GET'])
def signin_form():
    data = {
        "content": "authentication/sign-in.jinja",
    }

    return render_template('authentication.jinja', data=data, os=os)


@app.route("/signin", methods=['POST'])
def signin():
    data = {
        "content": "authentication/sign-in.jinja",
    }

    return render_template('authentication.jinja', data=data, os=os)


@app.route("/signout", methods=['POST'])
def signout():
    data = {
        "content": "authentication/sign-in.jinja",
    }

    return render_template('authentication.jinja', data=data, os=os)
