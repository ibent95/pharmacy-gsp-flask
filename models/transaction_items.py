import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func
#from models.transaction import TransactionModel


class TransactionItemsModel(db.Model):

    __tablename__ = 'transaksi_item'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    id_transaksi = db.Column(db.BigInteger, db.ForeignKey('transaksi.id'))
    id_produk = db.Column(db.String(100))
    kode_produk = db.Column(db.String(100))
    nama_produk = db.Column(db.String(100))
    jumlah_produk = db.Column(db.Integer)
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, id_transaksi, id_produk, kode_produk, nama_produk, jumlah_produk):
        self.id_transaksi = id_transaksi
        self.id_produk = id_produk
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jumlah_produk = jumlah_produk

    def setObjectToDict(self):
        return {
            "id": self.id,
            "id_transaksi": self.id_transaksi,
            "id_produk": self.id_produk,
            "kode_produk": self.kode_produk,
            "nama_produk": self.nama_produk,
            "jumlah_produk": self.jumlah_produk,
            "uuid": self.uuid
        }