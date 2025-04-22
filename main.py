from src.get_email import get_email, remove_period
from src.ResumeSend import ResumeSend

from pathlib import Path


# Change according to your environment
html_file = "message.html"
pdf_file = "exemplo.pdf"


TEXT_PATH = Path(__file__).parent / "templates" / html_file
FILE_PATH = Path(__file__).parent / "assets" / pdf_file


def main():
    opening = str(input("Title of the job opening: ")).strip()
    platform = str(input("Platform that you found:  ")).strip()
    subject = str(input("Email subject: ")).strip()
    enterprise_name = str(input("Type the enterprise name: ")).strip()
    email_recipient = None

    resume_send = ResumeSend()
    resume_send.recipient = email_recipient
    resume_send.opening = opening
    resume_send.platform = platform
    resume_send.subject = subject
    resume_send.text_file = TEXT_PATH
    resume_send.file_path = FILE_PATH

    print("\nThis may take a while...")

    user_search = f"email rh empresa {enterprise_name}"

    emails_list = get_email(user_search)

    if not emails_list:
        print("No emails founded")
    else:
        print("Founded these emails: \n")
        for i in range(len(emails_list)):
            print(f"[{i}]: {emails_list[i]}")

    user_op = str(input("\nSend message to one of the founded emails?[Y/n]: "))

    if user_op not in "Yy":
        print("Finishing operation....")
        return

    user_choice = int(input("Choose by index [0, 1, ...]: "))
    email_cleaned = remove_period(emails_list[user_choice])
    print(f"\nEmail will sent to {email_cleaned}")
    confirm = str(input("Confirm?[Y/n]: "))

    if confirm in "Yy":
        email_recipient = email_cleaned
        resume_send.send_email()
    else:
        print("Finishing operation...")
        return


main()
