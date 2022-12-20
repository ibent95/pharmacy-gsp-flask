import os

from app import app, request, render_template, redirect, flash, url_for, login_required
from configs.database import db
from forms.user import UserForm
from models.user import UserModel


# User
@app.route("/user", methods=['GET'])
@login_required
def user():
    title = "Pengguna"
    page = request.args.get('page', 1, type=int)
    data = {
        "content": "user/main.jinja",
        "title": title,
    }

    users = UserModel.query.order_by(UserModel.id.desc()).paginate(page=page, per_page=app.config["ITEMS_PER_PAGE"], error_out=False)

    data['users'] = users

    return render_template('index.jinja', data = data, os = os)

@app.route("/user/create", methods=['GET'])
@app.route("/user/update/<uuid>", methods=['GET'])
@login_required
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
@login_required
def user_create(uuid = None):
    form = UserForm()

    if (form.validate_on_submit() == False):
        flash("Masukan data tidak valid.")

        for fieldName, errorMessages in form.errors.items():
            #flash(fieldName)
            for err in errorMessages:
                flash(err)

        if (uuid):
            return redirect(url_for('user_form', uuid=uuid))

        else:
            return redirect(url_for('user_form'))

    else:

        user = UserModel(request.form['nama_pengguna'], request.form['role'], request.form['username'], request.form['password'])
        user.set_password(request.form['password'])

        db.session.add(user)

        db.session.commit()

    return redirect(url_for('user'))

@app.route("/user/manage/<uuid>", methods=['GET', 'POST'])
@login_required
def user_update(uuid = None):
    form = UserForm()

    if (form.validate_on_submit() == False):
        flash("Masukan data tidak valid.")

        for fieldName, errorMessages in form.errors.items():
            #flash(fieldName)
            for err in errorMessages:
                flash(err)

        if (uuid):
            return redirect(url_for('user_form', uuid=uuid))

        else:
            return redirect(url_for('user_form'))

    else:

        if (uuid) :
            user = UserModel.query.filter_by(uuid=uuid).first()

            user.nama_pengguna = request.form['nama_pengguna']
            user.role = request.form['role']
            user.username = request.form['username']
            user.password = request.form['password']
            user.set_password(request.form['password'])

        db.session.commit()

    return redirect(url_for('user'))

@app.route("/user/manage/<uuid>/delete", methods=['GET', 'POST'])
@login_required
def user_delete(uuid = None):

    # Delete
    if (uuid):

        user = UserModel.query.filter_by(uuid=uuid).first()

        db.session.delete(user)

        db.session.commit()

    else:

        flash('There is no id.')

    return redirect(url_for('user'))