from get_email import get_email
from send_email import ResumeSend

from pathlib import Path

FILE_PATH = Path(__file__).parent.parent / "utils" / "message.html"


def main():
    enterprise_name = str(input("Type the enterprise name: "))
    opening = str(input("Title of the job opening: "))
    platform = str(input("Platform that you found:  "))
    subject = str(input("Email subject: "))

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

    resume_send = ResumeSend()
    resume_send.recipient = email_recipient
    resume_send.opening = opening
    resume_send.platform = platform
    resume_send.subject = subject
    resume_send.file = FILE_PATH

    resume_send.send_email()


main()
