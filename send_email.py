import os
import pathlib
import smtplib

from string import Template
from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

FILE_PATH = pathlib.Path(__file__).parent / "utils" / "message.html"

sender = os.getenv("FROM_EMAIL", "CHANGE-ME")
recipient = sender


smtp_server = os.getenv("SMTP_SERVER", "")
smtp_port = int(os.getenv("SMTP_PORT", ""))

smtp_username = os.getenv("FROM_EMAIL", "")
smtp_password = os.getenv("EMAIL_PASSWORD", "")

with open(FILE_PATH, "r") as file:
    text_file = file.read()
    template = Template(text_file)
    text_email = template.substitute(vaga="Estágio", plataforma="LinkedIn")


email_subject = "Candidatura à vaga de Estágio Suporte A Aplicações - Luis Otávio Dias"

mime_multipart = MIMEMultipart()
mime_multipart["from"] = sender
mime_multipart["to"] = recipient
mime_multipart["subject"] = email_subject
mime_multipart["Content-Type"] = "text/html; charset=UTF-8"

email_body = MIMEText(text_email, "html", "utf-8")
mime_multipart.attach(email_body)


with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print("Email enviado!")
