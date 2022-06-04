import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func


class UserModel(db.Model):

    __tablename__ = 'pengguna'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    nama_pengguna = db.Column(db.String(100))
    role = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=True)
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, kode_produk, nama_produk):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk