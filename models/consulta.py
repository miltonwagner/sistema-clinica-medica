from extensions import db

class Consulta(db.Model):
    __tablename__ = "consulta"

    id = db.Column(db.Integer, primary_key=True)

    paciente_id = db.Column(db.Integer, db.ForeignKey("paciente.id"), nullable=False)
    medico_id = db.Column(db.Integer, db.ForeignKey("medico.id"), nullable=False)

    data = db.Column(db.String(20), nullable=False)
    hora = db.Column(db.String(10), nullable=False)

    status = db.Column(db.String(20), default="Agendada")

    # 🔥 RELACIONAMENTOS (CORREÇÃO DO ERRO)
    paciente = db.relationship("Paciente", backref="consultas")
    medico = db.relationship("Medico", backref="consultas")
