import os
import smtplib


from string import Template
from dotenv import load_dotenv
from pathlib import Path

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dataclasses import dataclass

load_dotenv()


@dataclass(init=False, repr=False)
class ResumeSend:
    """
    Won't work unless .env file is configured.
    Follow the .env-example to set up yours
    """

    opening: str
    platform: str
    subject: str
    recipient: str | None = None
    file: Path

    def send_email(self):
        file_path = self.file

        sender = os.getenv("FROM_EMAIL", "CHANGE-ME")

        if self.recipient is None:
            recipient = sender
        else:
            recipient = self.recipient

        smtp_server = os.getenv("SMTP_SERVER", "")
        smtp_port = int(os.getenv("SMTP_PORT", ""))

        smtp_username = os.getenv("FROM_EMAIL", "")
        smtp_password = os.getenv("APP_PASSWORD", "")

        with open(file_path, "r", encoding="utf-8") as file:
            text_file = file.read()
            template = Template(text_file)
            text_email = template.substitute(
                opening=self.job_opening,
                platform=self.platform,
            )

        mime_multipart = MIMEMultipart()
        mime_multipart["from"] = sender
        mime_multipart["to"] = recipient
        mime_multipart["subject"] = self.subject
        mime_multipart["Content-Type"] = "text/html; charset=UTF-8"

        email_body = MIMEText(text_email, "html", "utf-8")
        mime_multipart.attach(email_body)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, recipient, mime_multipart.as_string())
            print("Email sent!")
