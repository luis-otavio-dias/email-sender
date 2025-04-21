from src.get_email import get_email
from src.send_email import ResumeSend

from pathlib import Path


# Change according to your environment
html_file = "message.html"
pdf_file = "exemplo.pdf"


TEXT_PATH = Path(__file__).parent / "templates" / html_file
FILE_PATH = Path(__file__).parent / "assets" / pdf_file


def main():
    opening = str(input("Title of the job opening: "))
    platform = str(input("Platform that you found:  "))
    subject = str(input("Email subject: "))
    enterprise_name = str(input("Type the enterprise name: "))
    print("\nThis may take a while...")

    user_search = f"email do rh da empresa {enterprise_name}"

    emails_list = get_email(user_search)

    if not emails_list:
        print("No emails founded")
    else:
        print("Founded these emails")
        for i in range(len(emails_list)):
            print(f"{emails_list[i]}\n")
            if "rh" in emails_list[i]:
                print("You want to send a message to this email?")
                user_op = str(input("Y/n: "))
                if user_op == "Y":
                    email_recipient = emails_list[i]
                else:
                    continue

        user_op = str(input("Send the message to one of the founded emails?[Y/n]: "))
        if user_op == "Y":
            user_choice = int(input("Choose by index [0, 1, ...]: "))
            email_recipient = emails_list[user_choice]
        else:
            print("The email will sent to yourself.")
            email_recipient = None

    resume_send = ResumeSend()
    resume_send.recipient = email_recipient
    resume_send.opening = opening
    resume_send.platform = platform
    resume_send.subject = subject
    resume_send.text_file = TEXT_PATH
    resume_send.file_path = FILE_PATH

    resume_send.send_email()


main()
