import smtplib
import ssl
import os


def email_send(message):
    host = 'smtp.gmail.com'
    port = 465
    sender = 'example@gmail.com'
    receiver = 'example@gmail.com'
    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
