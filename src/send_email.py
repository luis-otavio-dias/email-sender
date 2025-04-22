import os
import smtplib


from string import Template
from dotenv import load_dotenv
from pathlib import Path

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

from dataclasses import dataclass

load_dotenv()


@dataclass(init=False, repr=False)
class ResumeSend:
    """
    Represents the necessary information to send a resume by email.
    Won't work unless .env file is configured.
    Follow the .env-example to set up yours

    Attributes subject and platform will be used to $-substitutions in text_file

    Attributes:
        opening (str): Title of the job opening.
        platform (str): Platform or website where the vacancy was found.
        subject (str): Subject of the email to be sent.
        recipient (str, optional): Recipient email adress. If None, the email will be sent to yourself.
        text_file (Path): HTML file with email body text.
        file_path (Path): Your reusume file, preferably pdf

    """

    opening: str
    platform: str
    subject: str
    recipient: str | None = None
    text_file: Path
    file_path: Path

    def send_email(self) -> None:
        """
        Public method. Structures the email message and sends it.
        """
        text_file = self.text_file
        file_path = self.file_path

        sender = os.getenv("FROM_EMAIL", "CHANGE-ME")

        if self.recipient is None:
            recipient = sender
        else:
            recipient = self.recipient

        smtp_server = os.getenv("SMTP_SERVER", "")
        smtp_port = int(os.getenv("SMTP_PORT", ""))

        smtp_username = os.getenv("FROM_EMAIL", "")
        smtp_password = os.getenv("APP_PASSWORD", "")

        mime_multipart = MIMEMultipart()
        mime_multipart["from"] = sender
        mime_multipart["to"] = recipient
        mime_multipart["subject"] = self.subject
        mime_multipart["Content-Type"] = "text/html; charset=UTF-8"

        with open(text_file, "r", encoding="utf-8") as file:
            text = file.read()
            template = Template(text)
            text_email = template.substitute(
                opening=self.opening,
                platform=self.platform,
            )

        email_body = MIMEText(text_email, "html", "utf-8")
        mime_multipart.attach(email_body)

        with open(file_path, "rb") as file:
            file_to_send = file.read()

        file_name = os.path.basename(file_path)
        file_to_attach = MIMEApplication(file_to_send, name=file_name)
        mime_multipart.attach(file_to_attach)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, recipient, mime_multipart.as_string())
            print("Sent!")
