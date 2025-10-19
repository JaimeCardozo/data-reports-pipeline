import os, smtplib, ssl
from email.message import EmailMessage

SMTP_SERVER = os.environ["SMTP_SERVER"]
SMTP_PORT   = int(os.environ.get("SMTP_PORT", "465"))
SMTP_USER   = os.environ["SMTP_USERNAME"]
SMTP_PASS   = os.environ["SMTP_PASSWORD"]
EMAIL_TO    = os.environ["EMAIL_TO"]

msg = EmailMessage()
msg["Subject"] = "Grupos Hermanos - Excel generado"
msg["From"] = SMTP_USER
msg["To"] = EMAIL_TO
msg.set_content("Adjunto el Excel generado automáticamente.")

with open("Grupos_Hermanos.xlsx", "rb") as f:
    data = f.read()
msg.add_attachment(data, maintype="application",
                   subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                   filename="Grupos_Hermanos.xlsx")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)
print("✅ Correo enviado")