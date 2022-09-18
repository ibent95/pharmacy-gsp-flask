import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func


class GSPHistoryModel(db.Model):

    __tablename__ = 'gsp_riwayat'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    nama_pengguna = db.Column(db.String(100))
    id_pengguna = db.Column(db.String(100))
    tanggal_mulai = db.Column(db.DateTime())
    tanggal_selesai = db.Column(db.DateTime())
    min_support = db.Column(db.String(100))
    tanggal_masuk = db.Column(db.DateTime())
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, nama_pengguna, id_pengguna, tanggal_mulai, tanggal_selesai, min_support, tanggal_masuk):
        self.nama_pengguna = nama_pengguna
        self.id_pengguna = id_pengguna
        self.tanggal_mulai = tanggal_mulai
        self.tanggal_selesai = tanggal_selesai
        self.min_support = min_support
        self.tanggal_masuk = tanggal_masuk