import os

from app import app, request, render_template, redirect, flash, url_for
from configs.database import db
from forms.drug import DrugForm
from models.drug import DrugModel

# Drug
@app.route("/drug", methods=['GET'])
def drug():
    title = "Obat"
    data = {
        "content": "drug/main.jinja",
        "title": title,
    }

    drugs = DrugModel.query.all()

    data['drugs'] = drugs

    return render_template('index.jinja', data = data, os = os)

@app.route("/drug/create", methods=['GET'])
@app.route("/drug/update/<uuid>", methods=['GET'])
def drug_form(uuid = None):
    title = "Formulir master data obat"
    data = {
        "content": "drug/form.jinja",
        "title": title,
        "form": DrugForm(),
        "drug": None
    }

    if (uuid) :
        data['drug'] = DrugModel.query.filter_by(uuid=uuid).first()

    return render_template('index.jinja', data=data, os=os)

@app.route("/drug/manage", methods=['GET', 'POST'])
def drug_create(uuid = None):

    form = DrugForm()

    # If form data is not valid
    if (form.validate_on_submit() == False):
        flash("Masukan data tidak valid.")

        for fieldName, errorMessages in form.errors.items():
            #flash(fieldName)
            for err in errorMessages:
                flash(err)

        if (uuid):
            return redirect(url_for('drug_form', uuid=uuid))

        else:
            return redirect(url_for('drug_form'))

    # If form data is valid
    else:

        drug = DrugModel(request.form['kode_produk'], request.form['nama_produk'], request.form['jumlah'])

        db.session.add(drug)

        db.session.commit()

    return redirect(url_for('drug'))

@app.route("/drug/manage/<uuid>", methods=['GET', 'POST'])
def drug_update(uuid = None):

    form = DrugForm()

    # If form data is not valid
    if (form.validate_on_submit() == False):
        flash("Masukan data tidak valid.")

        for fieldName, errorMessages in form.errors.items():
            #flash(fieldName)
            for err in errorMessages:
                flash(err)

        if (uuid):
            return redirect(url_for('drug_form', uuid=uuid))

        else:
            return redirect(url_for('drug_form'))

    # If form data is valid
    else:

        # Update (PUT)
        if (uuid):

            drug = DrugModel.query.filter_by(uuid=uuid).first()

            drug.kode_produk = request.form['kode_produk']
            drug.nama_produk = request.form['nama_produk']
            drug.jumlah = request.form['jumlah']

            db.session.commit()

        else:
            flash('There is no id.')
            return redirect(url_for('drug'))


    return redirect(url_for('drug'))

@app.route("/drug/manage/<uuid>/delete", methods=['GET', 'POST'])
def drug_delete(uuid = None):

    # Delete
    if (uuid):

        drug = DrugModel.query.filter_by(uuid=uuid).first()

        db.session.delete(drug)

        db.session.commit()

    else:

        flash('There is no id.');

    return redirect(url_for('drug'))