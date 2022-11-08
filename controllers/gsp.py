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

    dataSets = [
        [
            frozenset({'Et-950'}), frozenset({'Et-950'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'am-112'}), frozenset({'am-347'}), frozenset({'Pc-922'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'ce-101'}), frozenset({'ce-101'}), frozenset({'ce-101'}), frozenset({'ce-101'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'hu-625'}), frozenset({'hu-625'}), frozenset({'hu-625'}), frozenset({'hu-625'}), frozenset({'am-112'}), frozenset({'am-112'}), frozenset({'Fl-970'}), frozenset({'Fl-970'}), frozenset({'Vi-207'}), frozenset({'Vi-207'})
        ],
        [
            frozenset({'Sp-171'}), frozenset({'Sp-171'}), frozenset({'Sp-171'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'hu-625'}), frozenset({'hu-625'}), frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'om-797'}), frozenset({'om-797'}), frozenset({'om-797'}), frozenset({'om-797'}), frozenset({'vi-672'}), frozenset({'vi-672'}), frozenset({'vi-672'})
        ],
        [
            frozenset({'co-195'}), frozenset({'co-195'}), frozenset({'Do-439'}), frozenset({'Do-439'}), frozenset({'Do-439'}), frozenset({'Do-439'}), frozenset({'la-511'}), frozenset({'la-511'}), frozenset({'la-511'}), frozenset({'la-511'}), frozenset({'la-511'})
        ],
        [
            frozenset({'co-195'}), frozenset({'co-195'}), frozenset({'Ct-826'}), frozenset({'Ct-826'}), frozenset({'Ct-826'}), frozenset({'Ct-826'}), frozenset({'Gl-286'}), frozenset({'Gl-286'}), frozenset({'Gl-286'})
        ],
        [
            frozenset({'in-760'}), frozenset({'Sp-171'}), frozenset({'Sp-171'}), frozenset({'Sp-171'}), frozenset({'As-195'}), frozenset({'As-195'}), frozenset({'As-195'}), frozenset({'As-195'}), frozenset({'am-112'}), frozenset({'am-112'}), frozenset({'am-112'})
        ],
        [
            frozenset({'in-861'}), frozenset({'in-861'}), frozenset({'Pc-922'}), frozenset({'Th-452'}), frozenset({'Th-452'}), frozenset({'Th-452'})
        ],
        [
            frozenset({'Do-439'}), frozenset({'Do-439'}), frozenset({'Do-439'}), frozenset({'om-797'}), frozenset({'om-797'}), frozenset({'an-150'}), frozenset({'an-150'})
        ],
        [
            frozenset({'in-760'}), frozenset({'am-690'}), frozenset({'Do-439'}), frozenset({'Do-439'}), frozenset({'Do-439'})
        ],
        [
            frozenset({'lo-158'}), frozenset({'lo-158'}), frozenset({'lo-158'}), frozenset({'lo-158'}), frozenset({'hy-900'})
        ],
        [
            frozenset({'yu-772'}), frozenset({'Gl-286'}), frozenset({'Gl-286'}), frozenset({'Gl-286'}), frozenset({'Gl-286'}), frozenset({'Ct-826'}), frozenset({'Ct-826'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'am-112'}), frozenset({'am-112'}), frozenset({'am-112'}), frozenset({'am-112'}), frozenset({'am-347'}), frozenset({'am-347'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'pr-847'})
        ],
        [
            frozenset({'in-760'}), frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'Be-860'}), frozenset({'Be-860'}), frozenset({'Be-860'}), frozenset({'Be-860'})
        ],
        [
            frozenset({'an-150'}), frozenset({'Gl-286'}), frozenset({'Gl-286'}), frozenset({'Vi-207'}), frozenset({'Vi-207'}), frozenset({'Vi-207'}), frozenset({'yu-772'}), frozenset({'yu-772'}), frozenset({'Mu-216'}), frozenset({'Mu-216'}), frozenset({'Mu-216'})
        ],
        [
            frozenset({'Gl-286'}), frozenset({'Gl-286'}), frozenset({'Gl-286'}), frozenset({'Gl-286'})
        ],
        [
            frozenset({'Pr-622'}), frozenset({'Pr-622'}), frozenset({'Pr-622'}), frozenset({'to-886'}), frozenset({'Gl-286'}), frozenset({'Pr-622'}), frozenset({'Di-200'})
        ],
        [
            frozenset({'pc-746'}), frozenset({'in-798'}), frozenset({'Do-439'})
        ],
        [
            frozenset({'ke-202'}), frozenset({'me-225'})
        ],
        [
            frozenset({'pr-688'}), frozenset({'pr-688'}), frozenset({'pr-688'}), frozenset({'Er-149'}), frozenset({'ce-494'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'pc-746'}), frozenset({'Vi-207'}), frozenset({'Vi-207'}), frozenset({'Vi-207'})
        ],
        [
            frozenset({'Et-950'}), frozenset({'Et-950'}), frozenset({'Di-200'}), frozenset({'Di-200'}), frozenset({'Di-200'})
        ],
        [
            frozenset({'in-760'}), frozenset({'Me-715'}), frozenset({'Me-715'}), frozenset({'na-730'}), frozenset({'na-730'}), frozenset({'na-730'}), frozenset({'Vi-207'})
        ],
        [
            frozenset({'ke-202'}), frozenset({'pr-688'}), frozenset({'pr-688'}), frozenset({'ce-494'}), frozenset({'ce-494'}), frozenset({'ce-494'}), frozenset({'lo-158'}), frozenset({'lo-158'}), frozenset({'lo-158'}), frozenset({'lo-158'})
        ],
        [
            frozenset({'in-861'}), frozenset({'Th-452'}), frozenset({'Et-950'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'yu-772'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'an-150'})
        ],
        [
            frozenset({'am-690'}), frozenset({'am-690'})
        ],
        [
            frozenset({'am-347'}), frozenset({'am-347'}), frozenset({'am-347'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'Ct-826'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'})
        ],
        [
            frozenset({'me-225'}), frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'ce-494'}), frozenset({'lo-158'}), frozenset({'Di-200'}), frozenset({'Di-200'})
        ],
        [
            frozenset({'am-690'}), frozenset({'He-944'}), frozenset({'He-944'})
        ],
        [
            frozenset({'in-419'}), frozenset({'in-419'}), frozenset({'an-150'}), frozenset({'an-150'}), frozenset({'an-150'}), frozenset({'an-150'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'Ne-642'})
        ],
        [
            frozenset({'Be-860'}), frozenset({'Do-439'}), frozenset({'Do-439'}), frozenset({'am-690'})
        ],
        [
            frozenset({'am-690'}), frozenset({'An-908'})
        ],
        [
            frozenset({'am-690'}), frozenset({'Be-860'}), frozenset({'Be-860'})
        ],
        [
            frozenset({'Vi-207'}), frozenset({'Vi-207'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'Vi-207'}), frozenset({'Vi-207'}), frozenset({'Vi-207'}), frozenset({'Vi-207'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'In-733'}), frozenset({'An-908'}), frozenset({'An-908'}), frozenset({'An-908'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'om-267'}), frozenset({'om-267'}), frozenset({'om-267'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'Gl-286'}), frozenset({'Gl-286'}), frozenset({'Gl-286'}), frozenset({'Gl-286'})
        ],
        [
            frozenset({'am-690'}), frozenset({'As-195'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'vi-672'}), frozenset({'vi-672'}), frozenset({'vi-672'}), frozenset({'vi-672'}), frozenset({'vi-672'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'om-121'}), frozenset({'om-121'})
        ],
        [
            frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'ca-720'}), frozenset({'Be-860'}), frozenset({'Be-860'}), frozenset({'Be-860'})
        ],
        [
            frozenset({'As-195'}), frozenset({'ra-877'}), frozenset({'ra-877'}), frozenset({'ra-877'})
        ],
        [
            frozenset({'am-347'}), frozenset({'am-347'}), frozenset({'am-347'}), frozenset({'am-347'}), frozenset({'am-347'}), frozenset({'to-886'}), frozenset({'to-886'}), frozenset({'to-886'}), frozenset({'to-886'})
        ],
        [
            frozenset({'an-150'})
        ],
        [
            frozenset({'ra-877'}), frozenset({'ra-877'}), frozenset({'ra-877'}), frozenset({'ra-877'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'me-225'}), frozenset({'me-225'}), frozenset({'re-361'}), frozenset({'re-361'})
        ],
        [
            frozenset({'an-150'}), frozenset({'an-150'}), frozenset({'an-150'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'Me-715'}), frozenset({'Me-715'}), frozenset({'Me-715'}), frozenset({'Me-715'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'mo-433'}), frozenset({'mo-433'}), frozenset({'mo-433'})
        ],
        [
            frozenset({'in-760'}), frozenset({'al-187'}), frozenset({'re-903'}), frozenset({'re-903'}), frozenset({'re-903'})
        ],
        [
            frozenset({'ce-885'}), frozenset({'ib-258'}), frozenset({'ib-258'}), frozenset({'ib-258'})
        ],
        [
            frozenset({'in-760'}), frozenset({'me-225'}), frozenset({'me-225'}), frozenset({'me-225'})
        ],
        [
            frozenset({'om-267'}), frozenset({'ba-223'}), frozenset({'ba-223'})
        ],
        [
            frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'ca-720'}), frozenset({'ca-720'}), frozenset({'ca-720'}), frozenset({'ca-720'})
        ],
        [
            frozenset({'pr-688'}), frozenset({'am-347'}), frozenset({'am-347'}), frozenset({'am-347'})
        ],
        [
            frozenset({'am-112'}), frozenset({'am-112'})
        ],
        [
            frozenset({'an-150'})
        ],
        [
            frozenset({'in-760'}), frozenset({'re-903'})
        ],
        [
            frozenset({'in-760'}), frozenset({'pi-956'}), frozenset({'sa-485'}), frozenset({'sa-485'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'lo-158'}), frozenset({'lo-158'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'Ct-826'}), frozenset({'Ct-826'}), frozenset({'Ct-826'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'Sp-171'}), frozenset({'Sp-171'}), frozenset({'ce-654'}), frozenset({'ce-654'}), frozenset({'ce-654'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'Be-860'}), frozenset({'Be-860'}), frozenset({'Be-860'}), frozenset({'ca-720'}), frozenset({'ca-720'}), frozenset({'ca-720'})
        ],
        [
            frozenset({'an-150'}), frozenset({'an-150'}), frozenset({'an-150'}), frozenset({'an-150'})
        ],
        [
            frozenset({'am-112'}), frozenset({'am-112'}), frozenset({'am-112'}), frozenset({'am-112'})
        ],
        [
            frozenset({'in-798'}), frozenset({'an-150'}), frozenset({'an-150'}), frozenset({'an-150'})
        ],
        [
            frozenset({'am-690'})
        ],
        [
            frozenset({'in-419'}), frozenset({'No-321'}), frozenset({'Su-192'}), frozenset({'Su-192'}), frozenset({'pa-869'}), frozenset({'pa-869'}), frozenset({'pa-869'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'No-321'}), frozenset({'No-321'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'lo-158'}), frozenset({'hy-900'}), frozenset({'hy-900'})
        ],
        [
            frozenset({'an-150'})
        ],
        [
            frozenset({'am-347'}), frozenset({'am-347'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'Sp-171'}), frozenset({'Sp-171'}), frozenset({'Sp-171'}), frozenset({'Sp-171'})
        ],
        [
            frozenset({'si-182'}), frozenset({'si-182'})
        ],
        [
            frozenset({'si-182'}), frozenset({'gl-997'}), frozenset({'gl-997'})
        ],
        [
            frozenset({'am-690'})
        ],
        [
            frozenset({'in-621'}), frozenset({'in-621'}), frozenset({'Et-950'}), frozenset({'Et-950'}), frozenset({'Et-950'})
        ],
        [
            frozenset({'Vi-207'}), frozenset({'Vi-207'})
        ],
        [
            frozenset({'in-760'}), frozenset({'Fl-970'})
        ],
        [
            frozenset({'Do-439'}), frozenset({'pc-746'}), frozenset({'pc-746'})
        ],
        [
            frozenset({'Do-439'}), frozenset({'Do-439'})
        ],
        [
            frozenset({'in-621'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'Sp-171'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'As-195'}), frozenset({'As-195'}), frozenset({'As-195'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'va-411'})
        ],
        [
            frozenset({'am-690'})
        ],
        [
            frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'ca-720'}), frozenset({'ca-720'})
        ],
        [
            frozenset({'am-347'}), frozenset({'am-347'}), frozenset({'in-760'}), frozenset({'Pr-622'}), frozenset({'Pr-622'}), frozenset({'hu-625'})
        ],
        [
            frozenset({'am-112'})
        ],
        [
            frozenset({'in-760'}), frozenset({'vi-672'})
        ],
        [
            frozenset({'in-621'}), frozenset({'in-621'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'om-797'}), frozenset({'om-797'}), frozenset({'om-797'})
        ],
        [
            frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'am-347'}), frozenset({'am-347'}), frozenset({'am-347'}), frozenset({'am-347'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'ce-494'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'ce-795'}), frozenset({'ce-795'}), frozenset({'cy-457'}), frozenset({'cy-457'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'ac-490'}), frozenset({'ac-490'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'cy-334'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'om-267'}), frozenset({'om-267'}), frozenset({'pa-869'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-680'})
        ],
        [
            frozenset({'am-690'}), frozenset({'am-690'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'lo-158'}), frozenset({'lo-158'}), frozenset({'lo-158'}), frozenset({'lo-158'}), frozenset({'hy-900'}), frozenset({'hy-900'}), frozenset({'hy-900'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'am-112'}), frozenset({'am-112'}), frozenset({'me-225'}), frozenset({'me-225'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'gr-338'}), frozenset({'gr-338'}), frozenset({'me-530'}), frozenset({'me-530'}), frozenset({'Sp-171'}), frozenset({'Sp-171'}), frozenset({'Sp-171'})
        ],
        [
            frozenset({'ra-877'}), frozenset({'ra-877'}), frozenset({'ra-877'}), frozenset({'pr-847'}), frozenset({'pr-847'}), frozenset({'pr-847'}), frozenset({'pr-847'}), frozenset({'la-983'}), frozenset({'la-983'}), frozenset({'la-983'})
        ],
        [
            frozenset({'am-347'}), frozenset({'am-347'})
        ],
        [
            frozenset({'vo-523'}), frozenset({'vo-523'}), frozenset({'de-865'}), frozenset({'de-865'}), frozenset({'na-730'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'na-730'}), frozenset({'si-182'}), frozenset({'si-182'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'})
        ],
        [
            frozenset({'As-195'}), frozenset({'ra-877'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'al-187'}), frozenset({'re-903'}), frozenset({'pr-688'})
        ],
        [
            frozenset({'am-690'}), frozenset({'Be-860'})
        ],
        [
            frozenset({'in-760'}), frozenset({'na-730'}), frozenset({'na-730'}), frozenset({'Me-715'})
        ],
        [
            frozenset({'me-225'}), frozenset({'re-361'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'to-886'}), frozenset({'to-886'}), frozenset({'to-886'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-798'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'sa-984'}), frozenset({'sa-984'}), frozenset({'mo-433'}), frozenset({'mo-433'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'mo-433'})
        ],
        [
            frozenset({'am-690'}), frozenset({'am-690'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'Pr-622'}), frozenset({'Pr-622'}), frozenset({'Pr-622'})
        ],
        [
            frozenset({'am-690'})
        ],
        [
            frozenset({'cy-457'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'Do-439'}), frozenset({'Do-439'})
        ],
        [
            frozenset({'Fl-970'})
        ],
        [
            frozenset({'am-112'})
        ],
        [
            frozenset({'in-419'}), frozenset({'in-419'}), frozenset({'pa-869'}), frozenset({'pa-869'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'Pc-922'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'As-195'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'ra-877'}), frozenset({'ra-877'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-798'})
        ],
        [
            frozenset({'cy-457'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-798'})
        ],
        [
            frozenset({'ce-231'}), frozenset({'ce-231'})
        ],
        [
            frozenset({'in-564'}), frozenset({'al-187'}), frozenset({'de-865'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'Fl-970'})
        ],
        [
            frozenset({'Vi-207'})
        ],
        [
            frozenset({'in-861'})
        ],
        [
            frozenset({'in-798'}), frozenset({'om-797'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-798'}), frozenset({'pl-705'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-798'})
        ],
        [
            frozenset({'am-690'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-419'}), frozenset({'Su-192'})
        ],
        [
            frozenset({'in-419'})
        ],
        [
            frozenset({'in-798'})
        ],
        [
            frozenset({'in-798'}), frozenset({'pr-847'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-419'}), frozenset({'pa-869'}), frozenset({'pa-869'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-861'}), frozenset({'in-861'}), frozenset({'Th-452'}), frozenset({'Th-452'}), frozenset({'Et-950'}), frozenset({'Et-950'})
        ],
        [
            frozenset({'in-419'}), frozenset({'in-419'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'am-347'}), frozenset({'am-347'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'an-150'}), frozenset({'an-150'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-798'}), frozenset({'pr-555'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-419'})
        ],
        [
            frozenset({'an-150'}), frozenset({'an-150'}), frozenset({'an-150'})
        ],
        [
            frozenset({'Be-860'}), frozenset({'Be-860'}), frozenset({'Be-860'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'Pc-922'}), frozenset({'om-121'}), frozenset({'om-121'}), frozenset({'om-121'})
        ],
        [
            frozenset({'am-690'}), frozenset({'am-690'}), frozenset({'An-908'}), frozenset({'An-908'})
        ],
        [
            frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'}), frozenset({'in-798'})
        ],
        [
            frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'}), frozenset({'in-760'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-798'})
        ],
        [
            frozenset({'ce-494'})
        ],
        [
            frozenset({'vi-672'})
        ],
        [
            frozenset({'An-908'})
        ],
        [
            frozenset({'am-112'})
        ],
        [
            frozenset({'in-760'}), frozenset({'Bi-426'}), frozenset({'vi-342'})
        ],
        [
            frozenset({'in-798'})
        ],
        [
            frozenset({'in-760'})
        ],
        [
            frozenset({'in-798'}), frozenset({'br-230'})
        ],
        [
            frozenset({'in-760'}), frozenset({'am-433'}), frozenset({'om-267'})
        ],
        [
            frozenset({'Pc-922'}), frozenset({'gl-997'}), frozenset({'la-983'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'om-267'})
        ],
        [
            frozenset({'Pc-922'})
        ],
        [
            frozenset({'in-798'}), frozenset({'sp-342'})
        ],
        [
            frozenset({'ce-494'}), frozenset({'co-477'})
        ], [
            frozenset({'pr-688'}), frozenset({'om-678'})
        ]
    ]

    gspCalc = GSP(transactions=dataSets, minsup=0.01)
    result = gspCalc.run_alg()

    resultPreview = [
        {
            ('me-225',): 6, ('lo-158',): 6, ('in-419',): 8, ('pr-847',): 3, ('pa-869',): 4, ('Th-452',): 3, ('Do-439',): 8, ('to-886',): 3, ('Me-715',): 3, ('na-730',): 4, ('in-798',): 26, ('hu-625',): 3, ('yu-772',): 3, ('pc-746',): 3, ('vi-672',): 4, ('Be-860',): 7, ('Di-200',): 3, ('re-903',): 3, ('in-621',): 3, ('Vi-207',): 8, ('Sp-171',): 6, ('ce-494',): 6, ('Pr-622',): 3, ('An-908',): 4, ('am-347',): 10, ('As-195',): 6, ('ra-877',): 5, ('hy-900',): 3, ('in-861',): 4, ('an-150',): 12, ('Ct-826',): 4, ('pr-688',): 5, ('ca-720',): 4, ('cy-457',): 3, ('si-182',): 3, ('Gl-286',): 6, ('om-797',): 4, ('om-267',): 5, ('Fl-970',): 4, ('am-690',): 22, ('Et-950',): 5, ('Pc-922',): 29, ('in-760',): 91, ('al-187',): 3, ('mo-433',): 3, ('am-112',): 10
        },
        {
            ('Ct-826', 'Ct-826'): 3, ('Be-860', 'Be-860'): 5, ('an-150', 'an-150'): 7, ('in-419', 'in-419'): 3, ('in-760', 'Pc-922'): 3, ('ra-877', 'ra-877'): 4, ('Vi-207', 'Vi-207'): 6, ('in-760', 'Sp-171'): 3, ('in-760', 'in-760'): 45, ('me-225', 'me-225'): 3, ('in-798', 'in-798'): 11, ('Gl-286', 'Gl-286'): 5, ('Pr-622', 'Pr-622'): 3, ('Pc-922', 'Pc-922'): 13, ('am-690', 'Be-860'): 3, ('am-112', 'am-112'): 6, ('Sp-171', 'Sp-171'): 5, ('Do-439', 'Do-439'): 6, ('om-797', 'om-797'): 3, ('am-347', 'am-347'): 9, ('am-690', 'am-690'): 10, ('lo-158', 'hy-900'): 3, ('lo-158', 'lo-158'): 4, ('Et-950', 'Et-950'): 4, ('am-690', 'ca-720'): 3, ('pa-869', 'pa-869'): 3, ('ca-720', 'ca-720'): 3
        }
    ]

    Common.setLogger('info', 'GSP calculation test 2', {
        'result': result
    })

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
                #Common.setLogger('info', 'transactionItem ' + str(inc), transactionItem)
                count = 0
                while (count < int(transactionItem["jumlah_produk"])):
                    #Common.setLogger('info', 'transactionItem ' + str(inc) + ' count ' + str(count), {'code' : transactionItem["kode_produk"]})
                    groupData.append(frozenset({transactionItem["kode_produk"]}))
                    count += 1
                #for itemCount in range(0, int(transactionItem["jumlah_produk"])):
                #    transactionsGroupData.append(frozenset([transactionItem["kode_produk"]]))
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
                #Common.setPPrint('GSP calculation initial result', result)
                #Common.setLogger('info', 'GSP calculation result', result)

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
        #    'transaction': transactions,
        #    'data_sets': dataSets
        #})

        Common.setLogger('info', 'GSP calculation initial state', {
            'start_date': startDate,
            'end_date': endDate,
            'minimal_support': minSupport,
            #'transaction': transactions,
            'transaction_count': len(transactions),
            'data_sets': dataSets,
            'result': result,
        })

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