from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, DateTimeLocalField, FormField, FieldList
from wtforms.validators import InputRequired
from forms.transaction_product_list import TransactionProductListForm

class TransactionForm(FlaskForm):
    nomor_transaksi = StringField('No. Transaksi', validators=[InputRequired(message="Nomor transaksi harus diisi.")])
    tanggal_transaksi = DateTimeLocalField('Tanggal transaksi', validators=[InputRequired(message="Tanggal transaksi harus diisi.")], format="%Y-%m-%dT%H:%M", default= datetime.utcnow)
    nama_pelanggan = StringField('Nama pasien', validators=[InputRequired(message="Nama pasien / pelanggan harus diisi.")])
    daftar_produk = FieldList(FormField(TransactionProductListForm), 'Daftar produk', min_entries=1)
