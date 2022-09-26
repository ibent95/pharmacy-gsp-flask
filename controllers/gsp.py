import os, json, time

from app import app, request, render_template, make_response
from configs.database import db
from models.transaction import TransactionModel
from models.gsp_history import GSPHistoryModel
from marshmallow import Schema, fields
from forms.gsp import GSPForm
from operator import and_
from services.common import Common
from services.number import Number
from services.gsp import GSP
from fpdf import FPDF
from datetime import date, datetime


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
    page = request.args.get('page', 1, type=int)
    data = {
        "content": "gsp-contents/gsp.jinja",
        "title": title,
        "form": GSPForm(),
        "histories": [],
        "gsp_init_value": None,
    }

    histories = GSPHistoryModel.query.order_by(GSPHistoryModel.id.desc()).paginate(page, app.config["ITEMS_PER_PAGE"], False)

    data['histories'] = histories

    return render_template('index.jinja', data = data, os = os)

@app.route("/gsp-calculation-result", methods=['GET'])
def gsp_calculation_result():
    title = "Hasil perhitungan Generalized Sequential Pattern (GSP)"
    data = []
    historyUuid = None

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

                historyUuid = gspModel.uuid

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
        "transactions": [],
        "minimal_support": minSupport,
        "normalized_minimal_support": normalizedMinimalSupport,
        "history_uuid": historyUuid,
        "result": result
    }

    return render_template('index.jinja', data = data, os = os)

@app.route("/gsp-report/<uuid>", methods=['GET'])
def gsp_report(uuid=None):

    # Initial values
    dateTimeNow = datetime.now()
    dateTimeNowFormated = dateTimeNow.strftime("%Y-%m-%d-%H-%M-%S")
    fileName = "[" + dateTimeNowFormated + "] GSP-Report"
    fileExtention = "pdf"
    fileNameExtention = fileName + "." + fileExtention

    # GSP data
    history = GSPHistoryModel.query.filter_by(uuid=uuid).first()

    # save FPDF() class
    pdf = FPDF(format="A4")

    # Add a page
    pdf.add_page()

    # set style and size of font
    pdf.set_font("Arial", size=11)

    # create a cell
    pdf.cell(0, 7, "Hasil Perhitungan GSP (Generalized Sequential Pattern)", align='C', new_x="LEFT", new_y="NEXT")
    pdf.cell(0, 7, "Tanggal " + dateTimeNow.strftime("%Y-%m-%d"), align='C', new_x="LEFT", new_y="NEXT")

    resultTable = [
        ["No", "Pola", "Frekuensi"],
    ]

    for item in history.items:
        i = 1
        for resultItem in json.loads(item):
            resultTable.append([
                i,
                resultItem["data_set"],
                resultItem["frequency"],
            ])
            i = i + 1

    #i = 0
    #for result in resultTable :
    #    if (i == 0):
    #        for item in result:
    #            pdf.cell(0, 7, str(item), 1, new_x="END", new_y="TOP")
    #        pdf.ln(7)
    #    else:
    #        y = 0
    #        for item in result :
    #            if (y == 1):
    #                pdf.cell(0, 7, ", ".join(item), 1, new_x="END", new_y="TOP")
    #            else:
    #                pdf.cell(0, 7, str(item), 1, new_x="END", new_y="TOP")
    #            y = y + 1
    #        pdf.ln(7)
    #    i = i + 1

    line_height = pdf.font_size * 3.0
    col_width = pdf.epw / 5  # distribute content evenly
    for row in resultTable:
        y = 0
        for datum in row:
            if (y == 1):
                pdf.multi_cell(20, line_height, ", ".join(datum), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            else:
                pdf.multi_cell(20, line_height, str(datum), border=1, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        pdf.ln(line_height)

    # save the pdf with fileName .pdf
    response = make_response(pdf.output())
    response.headers.set('Content-Disposition', 'attachment', filename=fileNameExtention)
    response.headers.set('Content-Type', 'application/pdf')

    return response