import uuid

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.types import TypeDecorator

from app import app, environ

DB_CONNECTION = str(environ.get('DB_CONNECTION'))
DB_HOST = str(environ.get("DB_HOST"))
DB_PORT = str(environ.get("DB_PORT"))
DB_CONNECT_ARGS_HOST = str(environ.get("DB_CONNECT_ARGS_HOST"))
DB_CONNECT_ARGS_PORT = str(environ.get("DB_CONNECT_ARGS_PORT"))
DB_DATABASE = str(environ.get("DB_DATABASE"))
DB_USERNAME = str(environ.get("DB_USERNAME"))
DB_PASSWORD = str(environ.get("DB_PASSWORD"))

# SQLAlchemy database configuration with MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION + "://" + DB_USERNAME + ":" + DB_PASSWORD + "@" + DB_HOST + "/" + DB_DATABASE

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
#model = db.Model


class BinaryUUID(TypeDecorator):
    '''Optimize UUID keys. Store as 16 bit binary, retrieve as uuid.
    inspired by:
        http://mysqlserverteam.com/storing-uuid-values-in-mysql-tables/
    '''

    impl = BINARY(16)

    def process_bind_param(self, value, dialect):
        try:
            return value.bytes
        except AttributeError:
            try:
                return uuid(value).bytes
            except TypeError:
                # for some reason we ended up with the bytestring
                # ¯\_(ツ)_/¯
                # I'm not sure why you would do that,
                # but here you go anyway.
                return value

    def process_result_value(self, value, dialect):
        return uuid(bytes=value)
