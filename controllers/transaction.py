import os

from flask_sqlalchemy import SQLAlchemy
from app import app, request, render_template, redirect, flash, url_for
from configs.database import db
from forms.transaction import TransactionForm
from forms.transaction_product_list import TransactionProductListForm
from models.drug import DrugModel
from models.transaction import TransactionModel


# Transaction
@app.route("/transaction", methods=['GET'])
def transaction():
    title = "Transaksi"
    data = {
        "content": "transaction/main.jinja",
        "title": title,
        "transactions": [],
    }

    transactions = TransactionModel.query.all()

    data['transactions'] = transactions

    return render_template('index.jinja', data=data, os=os)


@app.route("/transaction/create", methods=['GET'])
@app.route("/transaction/update/<uuid>", methods=['GET'])
def transaction_form(uuid=None):
    title = "Formulir transaksi"
    transactionProductListForm = TransactionProductListForm(prefix='daftar_produk-_-')
    drugs = [(drug.kode_produk, drug.nama_produk) for drug in DrugModel.query.all()]
    data = {
        "content": "transaction/form.jinja",
        "title": title,
        "drugs": drugs,
        "form": TransactionForm(),
        "transaction": None
    }
    #data['form']['daftar_produk']['kode_produk']['coerce'] = int
    data['form'].daftar_produk[0].kode_produk.choices = transactionProductListForm.kode_produk.choices = drugs

    if (uuid):
        data['transaction'] = TransactionModel.query.filter_by(uuid=uuid).first()
        #data['transaction'].transaction

    return render_template('index.jinja', data=data, os=os, _transactionProductListFormTemplate=transactionProductListForm)


@app.route("/transaction/manage", methods=['GET', 'POST'])
@app.route("/transaction/manage/<uuid>", methods=['GET', 'POST'])
def transaction_manage(uuid=None):
    drugs = [(drug.kode_produk, drug.nama_produk) for drug in DrugModel.query.all()]
    form = TransactionForm()
    form.daftar_produk[0].kode_produk.choices = drugs

    print(request.form.getlist("daftar_produk"))

    if (form.validate_on_submit()):

        if (uuid):
            transaction = TransactionModel.query.filter_by(uuid=uuid).first()

            transaction.nomor_transaksi = request.form['nomor_transaksi']
            transaction.tanggal_transaksi = request.form['tanggal_transaksi']
            transaction.nomor_transaksi = request.form['nomor_transaksi']

            transaksi_item = []
            for produk in form.daftar_produk:
                transaksi_item = produk.kode_produk.data

            transaction.transaksi_item = transaksi_item

        else:
            print(request.form.getlist("daftar_produk"))
            transaction = TransactionModel(
                request.form['nomor_transaksi'],
                request.form['tanggal_transaksi'],
                request.form['nomor_transaksi'],
                request.form.getlist("daftar_produk")
            )

            db.session.add(transaction)

        db.session.commit()

    else:
        flash("Masukan data tidak valid.")

        if (uuid):
            return redirect(url_for('transaction_form', uuid=uuid))

        else:
            return redirect(url_for('transaction_form'))

    return redirect(url_for('transaction'))

    #render_template('index.jinja', data=data, os=os)
