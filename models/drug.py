import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func


class DrugModel(db.Model):

    __tablename__ = 'obat'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    kode_produk = db.Column(db.String(100), unique=True)
    nama_produk = db.Column(db.String(100))
    jumlah = db.Column(db.Integer())
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, kode_produk, nama_produk, jumlah):
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jumlah = jumlah

    def setObjectToDict(self):
        return {
            "id": self.id,
            "kode_produk": self.kode_produk,
            "nama_produk": self.nama_produk,
            "jumlah": self.jumlah,
            "uuid": self.uuid
        }