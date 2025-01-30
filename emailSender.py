import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time


def send_email(subject, body):
    try:
        sender_email = "sherlockbriefing@gmail.com"
        receiver_email = "pranumantri@gmail.com"
        text = f"Subject: {subject} \n\n {body}"
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, "ssfz tlro ibrw vazj")
        server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully")

    except Exception as e:
        print('Error sending email notification:', e)


def main():
    while True:
        print("email bot running")
        # Check current time against sending time
        hour = 16
        minute = 52
        if datetime.datetime.now().hour == hour and datetime.datetime.now().minute == minute:
            subject = 'Test email notification'
            body = 'hello! here will be some news and stuff. \n have a great day!'
            send_email(subject, body)

        # Wait for 1 minute before checking again
        time.sleep(60)


if __name__ == '__main__':
    main()
