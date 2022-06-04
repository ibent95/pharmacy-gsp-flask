from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class TransactionForm(FlaskForm):
    tanggal_transaksi = StringField('Tanggal transaksi', validators=[InputRequired()])
    nama_pelanggan = StringField('Nama pelanggan', validators=[InputRequired()])
