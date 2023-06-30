import os
import smtplib
import ssl


# Send email and secure username/ password using to send email by env
def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("E_USERNAME")
    password = os.getenv("PASSWORD")

    # Add any email to receive the email from contact me form
    receiver = "nayanadsem@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
