from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, DecimalField
from wtforms.validators import InputRequired, NumberRange


class GSPForm(FlaskForm):
    tanggal_mulai = DateField(
        'Tanggal mulai',
        validators=[
            InputRequired(
                message="Tanggal mulai harus diisi."
            )
        ],
        format="%Y-%m-%d",
        default=date(date.today().year, 1, 1)
    )

    tanggal_selesai = DateField(
        'Tanggal selesai',
        validators=[
            InputRequired(
                message="Tanggal selesai harus diisi."
            )
        ],
        format="%Y-%m-%d",
        default=date(date.today().year, 12, 31)
    )

    min_support = IntegerField(
        'Minimal support',
        validators=[
            InputRequired(
                message="Minimal support harus diisi."
            ),
            NumberRange(
                min=0,
            )
        ],
        default=15
    )
