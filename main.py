from src.get_email import get_email, remove_period
from src.ResumeSend import ResumeSend

from pathlib import Path


# Change according to your environment
html_file = "message.html"
pdf_file = "exemplo.pdf"


TEXT_PATH = Path(__file__).parent / "templates" / html_file
FILE_PATH = Path(__file__).parent / "assets" / pdf_file


def search_email(enterprise_name: str):
    print("\nThis may take a while...")

    user_search = f"rh email {enterprise_name}"

    emails_list = get_email(user_search)

    if not emails_list:
        emails_list.clear()
    else:
        print("Founded these emails: \n")
        for i in range(len(emails_list)):
            print(f"[{i}]: {emails_list[i]}")

    return emails_list


def main():
    resume_send = ResumeSend()
    resume_send.text_file = TEXT_PATH
    resume_send.file_path = FILE_PATH

    opening = str(input("Title of the job opening: ")).strip()
    platform = str(input("Platform that you found:  ")).strip()
    subject = str(input("Email subject: ")).strip()

    resume_send.opening = opening
    resume_send.platform = platform
    resume_send.subject = subject

    print("Select one: ")
    print("[0] Enter recipient manually\n[1] Search emails")

    user_op = int(input("Type 0 or 1: "))

    if user_op == 0:
        email_recipient = str(input("Email recipient: ")).strip()
        recipient = remove_period(email_recipient)

    elif user_op == 1:
        enterprise_name = str(input("Type the enterprise name: ")).strip()
        emails_list = search_email(enterprise_name)

        user_op = str(input("\nSend message to one of the founded emails?[Y/n]: "))

        if user_op not in "Yy":
            print("Finishing operation....")
            return

        user_choice = int(input("Choose by index [0, 1, ...]: "))
        recipient = remove_period(emails_list[user_choice])

    else:
        print("Invalid option")
        return

    print(f"\nEmail will be sent to {recipient}")
    confirm = str(input("Confirm?[Y/n]: "))

    if confirm in "Yy":
        resume_send.recipient = recipient
        resume_send.send_email()

    print("Finishing operation...")
    return


main()
