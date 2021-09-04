import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def remindcards(card):
    sender_email = "kopiv18@gmail.com"
    receiver_email = "bkopi95@gmail.com"
    #password = input("Type your password and press enter:")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Vehicle Card Reminder List"
    message["From"] = sender_email
    message["To"] = receiver_email
 

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    The Vehicle Card Numbers for reminding:
    \t{card_No}

    Thank You\
    """.format(card_No = '\n\t'.join(card))

    
    # Turn these into plain/html MIMEText objects
    msg = MIMEText(text, "plain")

    # Add attachment to message and convert message to string
    message.attach(msg)
    text = message.as_string()

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    

