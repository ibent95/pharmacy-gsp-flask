import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func
from sqlalchemy_serializer import SerializerMixin


class GSPHistoryTransactionItemsModel(db.Model, SerializerMixin):

    __tablename__ = 'gsp_riwayat_transaksi_item'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    id_gsp_riwayat = db.Column(db.BigInteger, db.ForeignKey('gsp_riwayat.id'))
    id_gsp_riwayat_transaksi = db.Column(db.BigInteger, db.ForeignKey('gsp_riwayat_transaksi.id'))
    id_transaksi = db.Column(db.BigInteger)
    id_produk = db.Column(db.BigInteger)
    kode_produk = db.Column(db.String(100))
    nama_produk = db.Column(db.String(100))
    jumlah_produk = db.Column(db.Integer)
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, id_gsp_riwayat, id_gsp_riwayat_transaksi, id_transaksi, id_produk, kode_produk, nama_produk, jumlah_produk):
        self.id_gsp_riwayat = id_gsp_riwayat
        self.id_gsp_riwayat_transaksi = id_gsp_riwayat_transaksi
        self.id_transaksi = id_transaksi
        self.id_produk = id_produk
        self.kode_produk = kode_produk
        self.nama_produk = nama_produk
        self.jumlah_produk = jumlah_produk