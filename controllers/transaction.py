from collections import namedtuple
from datetime import datetime
import os

from flask_sqlalchemy import SQLAlchemy
from app import app, request, render_template, redirect, flash, url_for
from configs.database import db
from pprint import pprint
from forms.transaction import TransactionForm
from forms.transaction_product_list import TransactionProductListForm
from models.drug import DrugModel
from models.transaction import TransactionModel
from models.transaction_items import TransactionItemsModel


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

    transactionProductListForm.kode_produk.choices = drugs

    if (uuid):
        data['transaction'] = TransactionModel.query.filter_by(uuid=uuid).first()

        transactionItemsFormDataGroup = namedtuple('transaksi_item', ['kode_produk', 'jumlah_produk', 'uuid'])
        transactionFormData = {
            'tanggal_transaksi': data['transaction'].tanggal_transaksi,
            'daftar_produk': []
        }

        for index, produk in enumerate(data['transaction'].transaksi_item):
            print(produk.kode_produk)
            transactionFormData['daftar_produk'].append(
                transactionItemsFormDataGroup(produk.kode_produk, produk.jumlah_produk, produk.uuid)
            )

        data['form'] = TransactionForm(data=transactionFormData)

    for produk in data['form'].daftar_produk:
        produk.kode_produk.choices = drugs

    return render_template('index.jinja', data=data, os=os, _transactionProductListFormTemplate=transactionProductListForm)

@app.route("/transaction/manage", methods=['GET', 'POST'])
def transaction_create(uuid=None):

    drugs = [(drug.kode_produk, drug.nama_produk) for drug in DrugModel.query.all()]
    form = TransactionForm()

    for produk in form.daftar_produk:
        produk.kode_produk.choices = drugs

    if (form.validate_on_submit() == False):

        for fieldName, errorMessages in form.errors.items():
            #flash(fieldName)
            for err in errorMessages:
                flash(err)

        if (uuid):
            return redirect(url_for('transaction_form', uuid=uuid))

        else:
            return redirect(url_for('transaction_form'))

    else:

        transaction = TransactionModel(
            request.form['nomor_transaksi'],
            request.form['tanggal_transaksi'],
            request.form['nama_pelanggan']
        )

        for produk in form.daftar_produk:
            drug = DrugModel.query.filter_by(kode_produk = produk.kode_produk.data).first()

            transaction.transaksi_item.append(
                TransactionItemsModel(
                    transaction.id,
                    drug.id,
                    drug.kode_produk,
                    drug.nama_produk,
                    produk.jumlah_produk.data
                )
            )

        db.session.add(transaction)

        db.session.commit()

    return redirect(url_for('transaction'))

@app.route("/transaction/manage/<uuid>", methods=['GET', 'POST'])
def transaction_update(uuid=None):

    drugs = [(drug.kode_produk, drug.nama_produk) for drug in DrugModel.query.all()]
    form = TransactionForm()

    for produk in form.daftar_produk:
        produk.kode_produk.choices = drugs

    if (form.validate_on_submit() == False):

        for fieldName, errorMessages in form.errors.items():

            for err in errorMessages:
                flash(err)

        if (uuid):
            return redirect(url_for('transaction_form', uuid=uuid))

        else:
            return redirect(url_for('transaction_form'))

    else:

        if (uuid):
            transaction = TransactionModel.query.filter_by(uuid=uuid).first()

            transaction.nomor_transaksi = request.form['nomor_transaksi']
            transaction.tanggal_transaksi = request.form['tanggal_transaksi']
            transaction.nama_pelanggan = request.form['nama_pelanggan']

            # Remove old data (Not good, but used for development speed)
            oldTransactionItem = TransactionItemsModel.query.filter_by(id_transaksi = transaction.id).delete()

            # Next improve is to change from old way (delete all old data and add all new dat) to new and proper way (update all old data and add new data)
            for index, produk in enumerate(form.daftar_produk):

                newDrugItem = DrugModel.query.filter_by(kode_produk = produk.kode_produk.data).first()

                #transactionItem = TransactionItemsModel.query.filter_by(kode_produk = produk.kode_produk.data, id_transaksi = transaction.id).first()

                #transactionItem['id_produk'] = newDrugItem.id
                #transactionItem['kode_produk'] = newDrugItem.kode_produk
                #transactionItem['nama_produk'] = newDrugItem.nama_produk
                #transactionItem['jumlah_produk'] = produk.jumlah_produk.data

                transaction.transaksi_item.append(
                    TransactionItemsModel(
                        transaction.id,
                        newDrugItem.id,
                        newDrugItem.kode_produk,
                        newDrugItem.nama_produk,
                        produk.jumlah_produk.data
                    )
                )

                # =====================================================================================================================================

                #if (produk.uuid.data):

                #    transaction.transaksi_item[index]['id_produk'] = drug.id
                #    transaction.transaksi_item[index]['kode_produk'] = drug.kode_produk
                #    transaction.transaksi_item[index]['nama_produk'] = drug.nama_produk
                #    transaction.transaksi_item[index]['jumlah_produk'] = produk.jumlah_produk.data

                #else:
                #    transaction.transaksi_item.append(
                #        TransactionItemsModel(
                #            transaction.id,
                #            drug.id,
                #            drug.kode_produk,
                #            drug.nama_produk,
                #            produk.jumlah_produk.data
                #        )
                #    )

            db.session.commit()

        else:

            flash('There is no id.')
            return redirect(url_for('drug'))


    return redirect(url_for('transaction'))

@app.route("/transaction/manage/<uuid>/delete", methods=['GET', 'POST'])
def transaction_delete(uuid=None):

    if (uuid):

        transaction = TransactionModel.query.filter_by(uuid=uuid).first()
        transactionItems = TransactionItemsModel.query.filter_by(id_transaksi = transaction.id).delete()

        db.session.delete(transaction)

        db.session.commit()

    else:

        flash('There is no id.')

    return redirect(url_for('transaction'))