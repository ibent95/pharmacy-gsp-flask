from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class DrugForm(FlaskForm):
    kode_produk = StringField('Kode produk', validators=[InputRequired()])
    nama_produk = StringField('Nama obat', validators=[InputRequired()])
