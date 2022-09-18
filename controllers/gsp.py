from json import dump
from operator import and_
from pprint import pprint
import os

from flask_sqlalchemy import SQLAlchemy
from app import app, request, platform, flask, render_template, jsonify
from configs.database import db
from services.common import Common
from traits.number import percentToFloat
from services.gsp import GSP
from forms.gsp import GSPForm
from sqlalchemy_querybuilder import Filter
from models.transaction import TransactionModel
from marshmallow import Schema, fields


## Schemas
class ProductSchema(Schema):
    id = fields.Str()
    id_transaksi = fields.Str()
    id_produk = fields.Str()
    kode_produk = fields.Str()
    nama_produk = fields.Str()
    jumlah_produk = fields.Str()
    uuid = fields.Str()

class TransactionSchema(Schema):
    id = fields.Str()
    nomor_transaksi = fields.Str()
    tanggal_transaksi = fields.Str()
    nama_pelanggan = fields.Str()
    transaksi_item = fields.Nested(ProductSchema())
    uuid = fields.Str()


# GSP Controllers
@app.route("/gsp", methods=['GET'])
def gsp():
    title = "Perhitungan (GSP)"
    data = {
        "content": "gsp-contents/gsp.jinja",
        "title": title,
        "form": GSPForm(),
        "gsp_init_value": None,

    }

    return render_template('index.jinja', data = data, os = os)

@app.route("/gsp-calculation-result", methods=['GET'])
def gsp_calculation_result():
    title = "Hasil perhitungan Generalized Sequential Pattern (GSP)"

    transactions = []
    dataSets = []
    result = []

    # Dates
    startDate = request.args.get('tanggal_mulai') + " 00:00:00"
    endDate = request.args.get('tanggal_selesai') + " 23:59:59"

    # Minimal support
    minSupport = request.args.get('min_support') if (request.args.get('min_support')) else 10

    if (startDate and endDate and minSupport):

        ## 1
        #transactionsRawData = TransactionModel.query.filter(
        #    and_(
        #        TransactionModel.tanggal_transaksi >= startDate,
        #        TransactionModel.tanggal_transaksi <= startDate
        #    )
        #).all()

        ## 2
        #rule = {
        #    "condition": "AND",
        #    "rules": [
        #        {
        #            "field": "transaksi.tanggal_transaksi",
        #            "type": "date",
        #            "operator": "greater_or_equal",
        #            "value": startDate
        #        },
        #        {
        #            "field": "transaksi.tanggal_transaksi",
        #            "type": "date",
        #            "operator": "less_or_equal",
        #            "value": endDate
        #        },
        #    ],
        #}
        #filter = Filter({ "transaksi": TransactionModel}, db.session.query())
        #print(filter.querybuilder(rule))

        #transactions = TransactionModel.query(
        #    filter.querybuilder(rule)
        #).all()

        ## 3
        transactionsRawData = TransactionModel.query.all()

        for transactionRawDataIndex, transactionRawData in enumerate(transactionsRawData) :

            transaction = TransactionSchema().dump(transactionRawData)
            transaction["transaksi_item"] = ProductSchema(many=True).dump(transactionRawData.transaksi_item) # => dict
            transaction_items = [(frozenset([transactionItem["kode_produk"]])) for transactionItem in transaction["transaksi_item"]]  # => tuple

            transactions.append(transaction)
            dataSets.append(transaction_items)

        normalizedMinimalSupport = percentToFloat(minSupport)

        if (transactions):
            gsp = GSP(transactions = dataSets, minsup = normalizedMinimalSupport)
            result = gsp.run_alg()
            Common.setPPrint('GSP calculation initial result', result)
            Common.setLogger('info', 'GSP calculation result', result)

        ## Set log and console message
        #Common.setPPrint('GSP calculation initial state', {
        #    'start_date': startDate,
        #    'end_date': endDate,
        #    'minimal_support': minSupport,
        #    'transaction': transactions,
        #    'data_sets': dataSets
        #})
        Common.setLogger('info', 'GSP calculation initial state', {
            'start_date': startDate,
            'end_date': endDate,
            'minimal_support': minSupport,
            'transaction': transactions,
            'data_sets': dataSets
        })

    data = {
        "content": "gsp-contents/gsp-results.jinja",
        "title": title,
        "start_date": startDate,
        "end_date": endDate,
        "transactions": transactions,
        "minimal_support": minSupport,
        "normalized_minimal_support": normalizedMinimalSupport,
        "result": result
    }

    a = [
        [frozenset({'A001'}), frozenset({'A003'})],
        [frozenset({'A001'}), frozenset({'A002'}), frozenset({'A003'})],
        [frozenset({'A002'}), frozenset({'A003'})],
        [frozenset({'A003'}), frozenset({'A003'}), frozenset({'A002'}), frozenset({'A001'})],
        [frozenset({'A001'}), frozenset({'A002'}), frozenset({'A003'})],
        [frozenset({'A001'}), frozenset({'A001'}), frozenset({'A002'}), frozenset({'A002'}), frozenset({'A003'}), frozenset({'A003'})],
        [frozenset({'A002'}), frozenset({'A003'})],
        [frozenset({'A001'}), frozenset({'A002'})],
        [frozenset({'A001'}), frozenset({'A002'})],
        [frozenset({'A001'}), frozenset({'A002'})],
        [frozenset({'A001'}), frozenset({'A002'})],
        [frozenset({'A001'}), frozenset({'A002'})],
        [frozenset({'A001'}), frozenset({'A002'})],
        [frozenset({'A001'}), frozenset({'A002'}), frozenset({'A003'})]
    ]

    return render_template('index.jinja', data = data, os = os)