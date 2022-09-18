import uuid

from configs.database import db, BinaryUUID
from sqlalchemy.sql.expression import func


class GSPHistoryItemsModel(db.Model):

    __tablename__ = 'gsp_riwayat_item'

    id = db.Column(db.BigInteger, primary_key=True, default=func.uuid_short())
    nama_pengguna = db.Column(db.String(100))
    role = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), unique=True)
    uuid = db.Column(db.String(36), unique=True, default=uuid.uuid4)

    def __init__(self, nama_pengguna, role, username, password):
        self.nama_pengguna = nama_pengguna
        self.role = role
        self.username = username
        self.password = password