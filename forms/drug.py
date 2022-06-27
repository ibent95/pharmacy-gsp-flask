from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from wtforms.validators import InputRequired, NumberRange


class DrugForm(FlaskForm):
    kode_produk = StringField('Kode produk', validators=[InputRequired()])
    nama_produk = StringField('Nama obat', validators=[InputRequired()])
    jumlah = IntegerField('Jumlah', validators=[InputRequired(), NumberRange(min=1, message="Hanya bisa diisi angka minimal 1.")])
