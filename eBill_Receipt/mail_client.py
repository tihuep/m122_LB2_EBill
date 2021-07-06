import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

def send_email(email, filename, invoice_nr, name, date):
    sender_mail = "ebill.hueppi.tbz@gmail.com"
    password = "Berufsschule8005!"

    message = MIMEMultipart()
    message['From'] = sender_mail
    message['To'] = email
    message['Subject'] = f'Erfolgte Verarbeitung Rechnung {invoice_nr}'

    message.attach(MIMEText(f'''Sehr geehrte(r) {name},

Am {str(date)} wurde die erfolgreiche Bearbeitung der Rechnung {invoice_nr}
vom Zahlungssystem <<TBZ Zahlsystem>> gemeldet.

Mit freundlichen Grüssen

Timon Hüppi
TBZ - Technische Berufsschule Zürich
''', 'plain'))
    attach_file = open(filename, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload(attach_file.read())
    encoders.encode_base64(payload)

    payload.add_header('Content-Decomposition', 'attachment', filename=filename)
    message.attach(payload)

    session = get_gmail_smtp_connection(sender_mail, password)

    text = message.as_string()
    result = session.sendmail(sender_mail, email, text)
    session.quit()

    return result

def get_gmail_smtp_connection(mail, password):
    port = 465
    smtp_server_domain_name = "smtp.gmail.com"
    ssl_context = ssl.create_default_context()
    service = smtplib.SMTP_SSL(smtp_server_domain_name, port, context=ssl_context)
    service.login(mail, password)
    return service