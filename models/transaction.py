from configs.database import db, model


class TransactionModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    kode = db.Column(db.String(100), unique=True)
    nama = db.Column(db.String(100))

    def __init__(self, kode, nama):
        print('Init transaction model')
        self.kode = kode
        self.nama = nama