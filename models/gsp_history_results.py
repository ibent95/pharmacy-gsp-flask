import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func
from sqlalchemy_serializer import SerializerMixin


class GSPHistoryResultsModel(db.Model, SerializerMixin):

    __tablename__ = 'gsp_riwayat_hasil'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    id_gsp_riwayat = db.Column(db.BigInteger, db.ForeignKey('gsp_riwayat.id'))
    data_set = db.Column(db.String(10000))
    frekuensi = db.Column(db.Integer)
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, id_gsp_riwayat, data_set, frekuensi):
        self.id_gsp_riwayat = id_gsp_riwayat
        self.data_set = data_set
        self.frekuensi = frekuensi