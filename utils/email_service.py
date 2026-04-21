import smtplib
from email.mime.text import MIMEText

def enviar_email(destino, nome, data, hora, medico):

    msg = MIMEText(f"""
Olá {nome},

Sua consulta foi agendada com sucesso.

Médico: {medico}
Data: {data}
Hora: {hora}

Clínica Médica
""")

    msg["Subject"] = "Confirmação de Consulta"
    msg["From"] = "clinica@sistema.com"
    msg["To"] = destino

    try:
        servidor = smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525)
        servidor.starttls()

        servidor.login(
            "9829e3f30a54aa",
            "dbda4137031405"
        )

        servidor.send_message(msg)
        servidor.quit()

    except Exception as e:
        print("Erro email:", e)