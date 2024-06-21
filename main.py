import smtplib
from email.mime.text import MIMEText

receiver_email = input("Enter the receiver's email: ")
message_content = input("Enter the message you want to send: ")

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'avoyan.mane2016@gmail.com'

msg = MIMEText(message_content)
msg['Subject'] = 'Automated Email'
msg['From'] = sender_email
msg['To'] = receiver_email

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    
    password = input("Enter your Gmail password and press Enter: ")
    server.login(sender_email, password)

    server.sendmail(sender_email, [receiver_email], msg.as_string())
