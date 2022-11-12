import os, json, time

from markupsafe import Markup

from app import app, request, url_for, render_template, make_response, login_required, json, Response
from configs.database import db
from flask_paginate import Pagination, get_page_args
from enumerations.common import GSPCalculationTypeEnum
from models.transaction import TransactionModel
from models.gsp_history import GSPHistoryModel
from marshmallow import Schema, fields
from forms.gsp import GSPForm
from operator import and_
from services.common import Common, RequestTypeConverter
from services.number import Number
from services.gsp import GSP
from fpdf import FPDF
from datetime import date, datetime


app.url_map.converters.update(request_type=RequestTypeConverter)

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
    transaksi_item = fields.List(fields.Nested("ProductSchema"))
    uuid = fields.Str()

# GSP Controllers
@app.route("/gsp", methods=['GET'])
@login_required
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

@app.route("/gsp/<request_type:calculation_type>", methods=['GET'])
@login_required
def gsp_training_testing_data(calculation_type):
    title = "Perhitungan (GSP)"
    page = request.args.get('page', 1, type=int)
    data = {
        "content": "gsp-contents/gsp-and-type.jinja",
        "title": title,
        "form": GSPForm(),
        "histories": [],
        "gsp_init_value": None,
        "calculation_type": calculation_type.value,
    }

    histories = GSPHistoryModel.query.order_by(GSPHistoryModel.id.desc()).paginate(page, app.config["ITEMS_PER_PAGE"], False)

    data['histories'] = histories

    return render_template('index.jinja', data = data, os = os)

@app.route("/gsp-calculation-result", methods=['GET', 'POST'])
@app.route("/gsp-calculation-result/<request_type:calculation_type>", methods=['GET', 'POST'])
@login_required
def gsp_calculation_result(calculation_type=None):
    title = "Hasil perhitungan Generalized Sequential Pattern (GSP)"
    csrfToken = request.form['csrf_token']
    #page = request.args.get('page', 1, type=int)
    #per_page = request.args.get('per_page', 10, type=int)
    data = []
    historyUuid = transactionsHistoriesPagination = None
    transactionsHistories = []
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    transactions = []
    dataSets = []
    result = []

    # Dates
    startDate = request.form['tanggal_mulai'] + " 00:00:00"
    endDate = request.form['tanggal_selesai'] + " 23:59:59"

    # Minimal support
    minSupport = request.form['min_support'] if (request.form['min_support']) else 10

    if (startDate and endDate and minSupport):

        if (calculation_type): Common.setPPrint('calculation_type', calculation_type.value)

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
        if (calculation_type == GSPCalculationTypeEnum.TRAINING):

            rawData = TransactionModel.query.filter(
                and_(
                    TransactionModel.tanggal_transaksi >= startDate,
                    TransactionModel.tanggal_transaksi <= endDate
                )
            )

            rawDataLimit = (90 * rawData.count()) / 100
            rawDataOffset = 0

            transactionsRawData = rawData.limit(rawDataLimit).offset(rawDataOffset).all()

        elif (calculation_type == GSPCalculationTypeEnum.TESTING):

            rawData = TransactionModel.query.filter(
                and_(
                    TransactionModel.tanggal_transaksi >= startDate,
                    TransactionModel.tanggal_transaksi <= endDate
                )
            )

            rawDataLimit = (10 * rawData.count()) / 100
            rawDataOffset = (90 * rawData.count()) / 100

            transactionsRawData = rawData.limit(rawDataLimit).offset(rawDataOffset).all()

        else:

            transactionsRawData = TransactionModel.query.filter(
                and_(
                    TransactionModel.tanggal_transaksi >= startDate,
                    TransactionModel.tanggal_transaksi <= endDate
                )
            ).all()

        #transactionsSerializeData = Common.listOfDictHelper(transactionsRawData)
        #transactionsJsonData = json.dumps(transactionsSerializeData, default=str)

        serializeData = []
        for transactionRawDataIndex, transactionRawData in enumerate(transactionsRawData):
            transaction = TransactionSchema().dump(transactionRawData)
            #transaction["transaksi_item"] = [ProductSchema().dump(produk) for produk in transactionRawData.transaksi_item] # => dict

            serializeData.append(transaction)

        transactionsJsonData = json.dumps(serializeData, default=str)

        #dataGroup = [[y for y in serializeData if y['tanggal_transaksi'] == x['tanggal_transaksi']] for x in serializeData]

        #for transactionGroup in dataGroup :
        transactionsGroupData = []
        for transaction in list(serializeData):
            #if (len(transaction["transaksi_item"]) == 1):
            #    groupData = []
            #    count = 0
            #    while (count < int(transaction["transaksi_item"][0]["jumlah_produk"])):
            #        groupData.append(transaction["transaksi_item"][0]["kode_produk"])
            #        count += 1

            #    transactionsGroupData.append(frozenset(groupData))

                #for itemCount in range(0, int(transaction["transaksi_item"][0]["jumlah_produk"])):
                #    transactionsGroupData.append(frozenset([transaction["transaksi_item"][0]["kode_produk"]]))
            #else:
            groupData = []
            inc = 1
            for transactionItem in transaction["transaksi_item"]:

                count = 0
                while (count < int(transactionItem["jumlah_produk"])):
                    groupData.append(frozenset({transactionItem["kode_produk"]}))
                    count += 1

                inc += 1

            transactionsGroupData.append(list(groupData))
            transactions.append(transaction)

        dataSets = list(transactionsGroupData)

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

                gspModel = GSPHistoryModel('Aku', 'Aku', startDate, endDate, minSupport, time.strftime('%Y-%m-%d %H:%M:%S'), transactionsJsonData, resultJsonData)
                db.session.add(gspModel)
                db.session.commit()

                historyUuid = gspModel.uuid
                transactionsHistories = Common.getDataPerPage(json.loads(transactionsJsonData), offset, per_page) ## Change the name to transaction later
                transactionsHistoriesPagination = Pagination(page=page, per_page=per_page, total=len(json.loads(transactionsJsonData))) ## Change the name to transaction later

        ## Set log and console message
        #Common.setPPrint('GSP calculation initial state', {
        #    'start_date': startDate,
        #    'end_date': endDate,
        #    'minimal_support': minSupport,
        #    #'transaction': transactions,
        #    'transaction_count': len(transactions),
        #    'data_sets': dataSets,
        #    'result': result,
        #})

        #Common.setLogger('info', 'GSP calculation initial state', {
        #    'start_date': startDate,
        #    'end_date': endDate,
        #    'minimal_support': minSupport,
        #    #'transaction': transactions,
        #    'transaction_count': len(transactions),
        #    'data_sets': dataSets,
        #    'result': result,
        #})

    data = {
        "content": "gsp-contents/gsp-results.jinja",
        "title": title,
        "start_date": startDate,
        "end_date": endDate,
        #"transactions": transaction,
        "csrf_token": csrfToken,
        "transactions": transactionsHistories if (transactionsHistories) else transactions ,
        "transactions_pagination": transactionsHistoriesPagination,
        "minimal_support": minSupport,
        "normalized_minimal_support": normalizedMinimalSupport,
        "history_uuid": historyUuid,
        "result": result
    }

    return render_template('index.jinja', data = data, os = os)

@app.route("/gsp-report/<uuid>", methods=['GET'])
@login_required
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

@app.route("/gsp-transactions/<uuid>", methods=['GET'])
def gsp_transaction(uuid):
    #page = request.args.get('page', 1, type=int)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    history = GSPHistoryModel.query.filter_by(uuid=uuid).first()
    transactions = json.loads(history.transactions)

    # Transactions data
    transactionsLimitData = Common.getDataPerPage(transactions, offset, per_page)

    # Start handle trabsaction data
    transactionsDataContainer = ""
    for transactionIndex, transaction in enumerate(transactionsLimitData):

        #Common.setPPrint('GSP transaction', transaction['transaksi_item'])

        transactionsDataContainer += "<div class='col col-md-3 col-sm-12 col-xs-12' style='margin-top: 15px;'><div class='table-responsive'>"
        transactionsDataContainer += "<h5>Transaksi " + str(transactionIndex + 1) + "</h5>"
        transactionsDataContainer += "<table><tbody><tr><td>No. Transaksi</td><td>:</td><td>" + transaction['nomor_transaksi'] + "</td></tr><tr><td>Nama pelanggan</td><td>:</td><td>" + transaction['nama_pelanggan'] + "</td></tr><tr><td>Tanggal transaksi</td><td>:</td><td>" + str(transaction['tanggal_transaksi']) + "</td></tr><tr><td>Jumlah produk</td><td>:</td><td>" + str(len(transaction['transaksi_item'])) + "</td></tr><tr><td>Daftar produk</td><td>:</td><td></td></tr></tbody></table>"
        transactionsDataContainer += "<table class='table table-secondary table-striped table-condensed'><thead style='display: block;'><tr><th style='width: 1%;'>No</th><th style='width: auto;'>Kode obat</th><th style='width: auto;'>Nama obat</th><th style='width: auto;'>Jumlah</th></tr></thead><tbody style='display: block; max-height: 479px !important; overflow-y: auto !important; overflow-x: hidden !important;'>"

        for dataSetIndex, data_set in enumerate(transaction['transaksi_item']):

            transactionsDataContainer += "<tr><td style='width: 1%;'>" + str(dataSetIndex + 1) + "</td><td style='width: auto;'>"
            transactionsDataContainer += "<div class='badge bg-light text-dark fw-bold lh-base'>" + data_set['kode_produk'] + "</div></td><td style='width: auto;'>"
            transactionsDataContainer += "<div class='badge bg-light text-dark fw-bold lh-base'>" + data_set['nama_produk'] + "</div></td><td style='width: auto;'>"
            transactionsDataContainer += "<div class='badge bg-light text-dark fw-bold lh-base'>" + data_set['jumlah_produk'] + "</div></td></tr>"

        transactionsDataContainer += "</tbody></table></div></div>"
    # End handle trabsaction data

    # Transactions pagination data
    transactionsPagination = Pagination(page=page, per_page=per_page, total=len(transactions))

    # Start handle pagination
    transactionsPaginationLinks = "<ul class='pagination justify-content-center'>"

    if transactionsPagination.has_prev :
        transactionsPaginationLinks += "<li class='page-item'><button class='page-link' onclick='getPageData(`" + url_for('gsp_transaction', uuid=uuid, page=transactionsPagination.page - 1, per_page=per_page) + "`)'>&laquo;</button></li>"

    for number in transactionsPagination.pages:

        if (transactionsPagination.page != number) :
            if (number != None):
                transactionsPaginationLinks += "<li class='page-item'><button class='page-link' onclick='getPageData(`" + url_for('gsp_transaction', uuid=uuid, page=number, per_page=per_page) + "`)'>" + str(number) + "</button></li>"
            else:
                transactionsPaginationLinks += "<li class='page-item disabled'><span class='page-link'>...</span></li>"

        else :
            transactionsPaginationLinks += "<li class='page-item active' aria-current='page'><span class='page-link'>" + str(number) + "</span></li>"

    if transactionsPagination.has_next:
        transactionsPaginationLinks += "<li class='page-item'><button class='page-link' onclick='getPageData(`" + url_for('gsp_transaction', uuid=uuid, page=transactionsPagination.page + 1, per_page=per_page) + "`)'>&raquo;</button></li>"

    transactionsPaginationLinks += "</ul>"
    # End handle pagination

    data = {
        "active_page_num": page,
        "transactions": transactionsLimitData,
        "transactions_container": transactionsDataContainer,
        "transactions_pagination_info": transactionsPagination.info,
        "transactions_pagination_links": transactionsPaginationLinks,
    }

    return Response(
        response = json.dumps({
            "data": data
        }),
        status = 201,
        mimetype = "application/json"
    )