from extensions import db

class Paciente(db.Model):
    __tablename__ = "paciente"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))