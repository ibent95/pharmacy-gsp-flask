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
@app.route("/drug/manage/<uuid>", methods=['GET', 'POST'])
def drug_manage(uuid = None):
    form = DrugForm()

    if (form.validate_on_submit() and (request.form['kode_produk'] == None or request.form['nama_produk'] == None)) :
        flash("Masukan data valid.")

        if (uuid):
            return redirect(url_for('drug_form', uuid=uuid))

        else:
            return redirect(url_for('drug_form'))

    elif (form.validate_on_submit() and (request.form['kode_produk'] and request.form['nama_produk'])):

        if (uuid) :
            drug = DrugModel.query.filter_by(uuid=uuid).first()

            drug.kode_produk = request.form['kode_produk']
            drug.nama_produk = request.form['nama_produk']

        else:
            drug = DrugModel(request.form['kode_produk'], request.form['nama_produk'])

            db.session.add(drug)

        db.session.commit()

    return redirect(url_for('drug'))

    #render_template('index.jinja', data=data, os=os)
