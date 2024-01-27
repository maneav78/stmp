import smtplib
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'avoyan.mane2016@gmail.com'
receiver_email = 'htarzyanh@gmail.com'
message = 'Python script-ov em es namaky uxarkel'

msg = MIMEText(message)
msg['Subject'] = 'Automated Email'
msg['From'] = sender_email
msg['To'] = receiver_email

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()

    password = input("Enter your Gmail password and press Enter: ")
    server.login(sender_email, password)

    server.sendmail(sender_email, [receiver_email], msg.as_string())
