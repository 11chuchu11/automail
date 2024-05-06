from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import ssl


def sendMail(email, password,to, subject, body, files=[]):
    SERVER_PORT=465
    
    em = MIMEMultipart()
    em['From'] = email
    em['To'] = to
    em["Subject"] = subject
    em.attach(MIMEText(body, 'plain'))

    for attached in files:
        with open(attached, 'rb') as file:
            attached_content = file.read()
        attached_mime = MIMEApplication(attached_content)
        filename= attached.split('/')[-1]
        attached_mime.add_header('Content-Disposition', 'attachment', filename=filename)
        em.attach(attached_mime)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', SERVER_PORT, context=context) as smtp:
        smtp.login(email, password)
        smtp.sendmail(email, to, em.as_string())