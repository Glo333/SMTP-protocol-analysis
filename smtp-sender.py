import smtplib
from email.mime.text import MIMEText

# Set up the SMTP server details
smtp_server = 'localhost'
smtp_port = 1025

# Create a MIMEText object with the email content
msg = MIMEText('This is a test email sent to the custom SMTP server.')

# Set the sender and recipient email addresses
msg['From'] = 'ibolarinwa606@gmail.com'
msg['To'] = 'bolaismail07@gmail.com'
msg['Subject'] = 'Test Email'

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.send_message(msg)
