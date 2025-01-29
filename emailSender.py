import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = ''
SENDER_PASSWORD = ''
RECIPIENT_EMAIL = 'skonanki05@gmail.com'


def send_email(subject, body):
    try:
        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        # Compose email message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send email
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        print('Email notification sent successfully!')

        # Close connection
        server.quit()
    except Exception as e:
        print('Error sending email notification:', e)


def main():
    while True:
        print("You will be notified on your E-mail daily by 9:00 AM")
        # Check if current time is 9:00 AM
        if datetime.datetime.now().hour == 13 and datetime.datetime.now().minute == 40:
            subject = 'Test email notification'
            body = 'hello! here will be some news and stuff. \n have a great day!'
            send_email(subject, body)

        # Wait for 1 minute before checking again
        time.sleep(60)


if __name__ == '__main__':
    main()
