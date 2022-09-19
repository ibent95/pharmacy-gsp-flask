import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func
from sqlalchemy_serializer import SerializerMixin
from models.gsp_history_transactions import GSPHistoryTransactionsModel
from models.gsp_history_results import GSPHistoryResultsModel


class GSPHistoryModel(db.Model, SerializerMixin):

    __tablename__ = 'gsp_riwayat'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    nama_pengguna = db.Column(db.String(100))
    id_pengguna = db.Column(db.String(100))
    tanggal_mulai = db.Column(db.DateTime())
    tanggal_selesai = db.Column(db.DateTime())
    min_support = db.Column(db.String(100))
    tanggal_masuk = db.Column(db.DateTime())
    gsp_history_transactions = db.relationship('GSPHistoryTransactionsModel', backref='gsp_riwayat')
    gsp_history_results = db.relationship('GSPHistoryResultsModel', backref='gsp_riwayat')
    transactions = db.Column(db.JSON)
    items = db.Column(db.JSON)
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, nama_pengguna, id_pengguna, tanggal_mulai, tanggal_selesai, min_support, tanggal_masuk, transactions, items):
        self.nama_pengguna = nama_pengguna
        self.id_pengguna = id_pengguna
        self.tanggal_mulai = tanggal_mulai
        self.tanggal_selesai = tanggal_selesai
        self.min_support = min_support
        self.tanggal_masuk = tanggal_masuk
        self.transactions = transactions
        self.items = items