import os, smtplib, ssl
from email.message import EmailMessage
from datetime import datetime


SMTP_SERVER = os.environ["SMTP_SERVER"]
SMTP_PORT   = int(os.environ.get("SMTP_PORT", "465"))
SMTP_USER   = os.environ["SMTP_USERNAME"]
SMTP_PASS   = os.environ["SMTP_PASSWORD"]
EMAIL_TO    = os.environ["EMAIL_TO"]

fecha_actual = datetime.now().strftime("%Y-%m-%d")

msg = EmailMessage()
msg["Subject"] = f"Grupos Hermanos - {fecha_actual}"
msg["From"] = SMTP_USER
msg["To"] = EMAIL_TO
msg.set_content(
    f"""
Hola 👋,

Adjunto el archivo Excel generado con los grupos de este mes.

📅 Fecha de generación: {fecha_actual}
📎 Archivo: Grupos_Celebraciones.xlsx

Saludos,
¡La paz!
"""
)

with open("Grupos_Celebraciones.xlsx", "rb") as f:
    data = f.read()
msg.add_attachment(data, maintype="application",
                   subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                   filename="Grupos_Celebraciones.xlsx")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)
print(f"✅ Correo enviado correctamente ({fecha_actual})")