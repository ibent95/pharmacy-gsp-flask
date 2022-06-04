import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func


class TransactionModel(db.Model):

    __tablename__ = 'transaksi'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    tanggal_transaksi = db.Column(db.DateTime())
    nama_pelanggan = db.Column(db.String(100))
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, tanggal_transaksi, nama_pelanggan):
        self.tanggal_transaksi = tanggal_transaksi
        self.nama_pelanggan = nama_pelanggan