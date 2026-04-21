from datetime import datetime, timedelta
from models.consulta import Consulta
from utils.email_service import enviar_email


def verificar_lembretes():

    hoje = datetime.now().date()
    amanha = hoje + timedelta(days=1)

    consultas = Consulta.query.all()

    for c in consultas:
        if c.status == "Agendada":

            data_consulta = datetime.strptime(c.data, "%Y-%m-%d").date()

            if data_consulta == amanha:
                print("🔔 Enviando lembrete...")

                enviar_email(
                    c.email,
                    c.paciente_nome,
                    c.data,
                    c.hora,
                    c.medico
                )
