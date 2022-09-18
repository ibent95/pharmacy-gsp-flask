import uuid

from itsdangerous import Serializer
from sqlalchemy import inspect

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func
from sqlalchemy.ext.declarative import as_declarative
from models.transaction_items import TransactionItemsModel


#@as_declarative()
class TransactionModel(db.Model):

    __tablename__ = 'transaksi'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    nomor_transaksi = db.Column(db.String(100))
    tanggal_transaksi = db.Column(db.DateTime())
    nama_pelanggan = db.Column(db.String(100))
    transaksi_item = db.relationship('TransactionItemsModel', backref='transaksi')
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, nomor_transaksi, tanggal_transaksi, nama_pelanggan):
        self.nomor_transaksi = nomor_transaksi
        self.tanggal_transaksi = tanggal_transaksi
        self.nama_pelanggan = nama_pelanggan
        #self.transaksi_item = transaksi_item

    def setObjectToDict(self):
        return {
            "id": self.id,
            "nomor_transaksi": self.nomor_transaksi,
            "tanggal_transaksi": self.tanggal_transaksi,
            "nama_pelanggan": self.nama_pelanggan,
            "transaksi_item": self.transaksi_item,
            "uuid": self.uuid
        }