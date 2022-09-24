from datetime import datetime
from operator import and_
from pprint import pprint
import os, json, time

from flask_sqlalchemy import SQLAlchemy
from app import app, request, platform, flask, render_template, jsonify
from configs.database import db
from models.gsp_history import GSPHistoryModel
from services.common import Common
#from services.json import DTEncoder
from services.number import Number
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

class DTEncoder(json.JSONEncoder):

    def default(self, obj):
        # 👇️ if passed in object is datetime object
        # convert it to a string
        if isinstance(obj, datetime):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


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
    data = []

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

        ## 2
        transactionsRawData = TransactionModel.query.filter(
            and_(
                TransactionModel.tanggal_transaksi >= startDate,
                TransactionModel.tanggal_transaksi <= endDate
            )
        ).all()

        transactionsSerializeData = Common.listOfDictHelper(transactionsRawData)
        transactionsJsonData = json.dumps(transactionsSerializeData, default=str)

        serializeData = []
        for transactionRawDataIndex, transactionRawData in enumerate(transactionsRawData):
            transaction = TransactionSchema().dump(transactionRawData)
            transaction["transaksi_item"] = ProductSchema(many=True).dump(transactionRawData.transaksi_item) # => dict

            serializeData.append(transaction)

        dataGroup = [[y for y in serializeData if y['tanggal_transaksi'] == x['tanggal_transaksi']] for x in serializeData]

        for transactionGroup in dataGroup :
            transactionsGroupData = []
            for transaction in list(transactionGroup):
                if (len(transaction["transaksi_item"]) == 1):
                    transaction_items = transaction["transaksi_item"][0]["kode_produk"]
                else:
                    transaction_items = frozenset([transactionItem["kode_produk"] for transactionItem in transaction["transaksi_item"]])

                transactionsGroupData.append(transaction_items)
                transactions.append(transaction)
            dataSets.append(transactionsGroupData)

        ## Normalize minimal support to float
        normalizedMinimalSupport = Number.percentToFloat(minSupport)

        ## GSP calculation
        if (transactions):
            gsp = GSP(transactions = dataSets, minsup = normalizedMinimalSupport)
            result = gsp.run_alg()

            ## For GSP`s` history
            if (result):
                resultJsonData = []
                for frequency_patterns in result:
                    resultJsonData.append(json.dumps([ { "data_set": data_set, "frequency": frequency } for data_set, frequency in frequency_patterns.items()]))
                #Common.setPPrint('GSP calculation initial result', result)
                Common.setLogger('info', 'GSP calculation result', result)

                gspModel = GSPHistoryModel('Aku', 'Aku', startDate, endDate, minSupport, time.strftime('%Y-%m-%d %H:%M:%S'), transactionsJsonData, resultJsonData)
                db.session.add(gspModel)
                db.session.commit()

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
            #'transaction': transactions,
            #'data_sets': dataSets
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

    return render_template('index.jinja', data = data, os = os)

@app.route("/gsp-report", methods=['GET'])
def gsp_report():
    return None