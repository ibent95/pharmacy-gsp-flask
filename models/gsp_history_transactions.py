import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func
from sqlalchemy_serializer import SerializerMixin
from models.gsp_history_transaction_items import GSPHistoryTransactionItemsModel


class GSPHistoryTransactionsModel(db.Model, SerializerMixin):

    __tablename__ = 'gsp_riwayat_transaksi'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    id_gsp_riwayat = db.Column(db.BigInteger, db.ForeignKey('gsp_riwayat.id'))
    id_transaksi = db.Column(db.BigInteger)
    tanggal_transaksi = db.Column(db.DateTime())
    gsp_history_transaction_items = db.relationship('GSPHistoryTransactionItemsModel', backref='gsp_riwayat_transaksi')
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, id_gsp_riwayat, id_transaksi, tanggal_transaksi):
        self.id_gsp_riwayat = id_gsp_riwayat
        self.id_transaksi = id_transaksi
        self.tanggal_transaksi = tanggal_transaksi