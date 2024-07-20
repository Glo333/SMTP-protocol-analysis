import smtplib
from email.mime.text import MIMEText

spoofed_sender = 'spoofed@example.com'
recipient = 'bolaismail07@gmail.com'

msg = MIMEText('This is a spoofed email.')

# Set the spoofed sender and actual recipient addresses in the email headers
msg['From'] = spoofed_sender
msg['To'] = recipient
msg['Subject'] = 'Spoofed Email'

# Connect to your custom SMTP server and send the spoofed email
with smtplib.SMTP('localhost', 1025) as server:
    server.send_message(msg)
