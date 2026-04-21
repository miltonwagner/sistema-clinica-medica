from extensions import db

class Medico(db.Model):
    __tablename__ = "medico"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    especialidade = db.Column(db.String(100))