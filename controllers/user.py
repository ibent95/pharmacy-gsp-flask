import os

from app import app, request, render_template, redirect, flash, url_for
from configs.database import db
from forms.user import UserForm
from models.user import UserModel


# User
@app.route("/user", methods=['GET'])
def user():
    title = "Pengguna"
    data = {
        "content": "user/main.jinja",
        "title": title,
    }

    users = UserModel.query.all()

    data['users'] = users

    return render_template('index.jinja', data = data, os = os)

@app.route("/user/create", methods=['GET'])
@app.route("/user/update/<uuid>", methods=['GET'])
def user_form(uuid = None):
    title = "Formulir master data pengguna"
    data = {
        "content": "user/form.jinja",
        "title": title,
        "form": UserForm(),
        "user": None
    }

    if (uuid) :
        data['user'] = UserModel.query.filter_by(uuid=uuid).first()

    return render_template('index.jinja', data=data, os=os)

@app.route("/user/manage", methods=['GET', 'POST'])
@app.route("/user/manage/<uuid>", methods=['GET', 'POST'])
def user_manage(uuid = None):
    form = UserForm()

    if (form.validate_on_submit() and (request.form['kode_produk'] == None or request.form['nama_produk'] == None)) :
        flash("Masukan data valid.")

        if (uuid):
            return redirect(url_for('user_form', uuid=uuid))

        else:
            return redirect(url_for('user_form'))

    elif (form.validate_on_submit() and (request.form['kode_produk'] and request.form['nama_produk'])):

        if (uuid) :
            user = UserModel.query.filter_by(uuid=uuid).first()

            user.kode_produk = request.form['kode_produk']
            user.nama_produk = request.form['nama_produk']

        else:
            user = UserModel(request.form['kode_produk'], request.form['nama_produk'])

            db.session.add(user)

        db.session.commit()

    return redirect(url_for('user'))

    #render_template('index.jinja', data=data, os=os)
