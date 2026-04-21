from extensions import db

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    idade = db.Column(db.Integer)
    telefone = db.Column(db.String(20))
    email = db.Column(db.String(100))


class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente_nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    medico = db.Column(db.String(100))
    especialidade = db.Column(db.String(100))
    data = db.Column(db.String(20))
    hora = db.Column(db.String(10))
    status = db.Column(db.String(20), default="Agendada")
