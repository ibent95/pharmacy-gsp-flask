import os, json

from app import app, platform, flask, request, jsonify, render_template, login_manager, login_user, logout_user, flash
from operator import and_
from models.user import UserModel
from services.common import Common

login_manager.login_view = 'signin'

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
    indexTemplate = 'authentication.jinja'

    username = request.form['username']
    password = request.form['password']

    user = UserModel.query.filter_by(username=username).first()

    # Check user
    if (user == None): # Username not found
        flash("Username tidak ditemukan!")
        Common.setPPrint('Sign in', 'username not found')

    if (user and (user.check_password(password) == False)): # Wrong password
        flash("Password salah!")
        Common.setPPrint('Sign in', 'wrong password')

    if (user and user.check_password(password)): # Username and password found

        #flash("Berhasil masuk!")

        login_user(user)

        data['content'] = 'home.jinja'

        indexTemplate = 'index.jinja'

    return render_template(indexTemplate, data=data, os=os)



@app.route("/signout", methods=['GET'])
def signout():
    data = {
        "content": "authentication/sign-in.jinja",
    }

    logout_user()

    return render_template('authentication.jinja', data=data, os=os)