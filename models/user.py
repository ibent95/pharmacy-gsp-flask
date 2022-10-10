import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model, SerializerMixin):

    __tablename__ = 'pengguna'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    nama_pengguna = db.Column(db.String(100))
    role = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(256), unique=True)
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, nama_pengguna, role, username, password):
        self.nama_pengguna = nama_pengguna
        self.role = role
        self.username = username
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def setObjectToDict(self):
        return {
            "id": self.id,
            "nama_pengguna": self.nama_pengguna,
            "role": self.role,
            "username": self.username,
            "password": self.password,
            "uuid": self.uuid,
        }