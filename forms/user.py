from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class UserForm(FlaskForm):
    nama_pengguna = StringField('Nama pengguna', validators=[InputRequired()])
    role = StringField('Peran (Role)', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
