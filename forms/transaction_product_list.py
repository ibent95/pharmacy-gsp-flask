from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, HiddenField
from wtforms.validators import InputRequired, NumberRange

from models.drug import DrugModel


class TransactionProductListForm(FlaskForm):
    kode_produk = SelectField('Produk', validators=[InputRequired(message="Produk harus diisi.")])
    jumlah_produk = IntegerField('Jumlah', validators=[InputRequired(message="Jumlah produk harus diisi."), NumberRange(min=1, max=50, message="Hanya bisa diisi angka minimal 1.")])
    uuid = HiddenField()

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(TransactionProductListForm, self).__init__(meta={'csrf':False}, *args, **kwargs)
    #    self.kode_produk.choices = [(drug.kode_produk, drug.nama_produk) for drug in DrugModel.query.all()]
