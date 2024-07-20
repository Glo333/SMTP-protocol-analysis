import smtpd
import asyncore
class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print(f'Incoming message from: {peer}')
        print(f'From: {mailfrom}')
        print(f'To: {rcpttos}')
        print(f'Data:\n{data}')
        return

server = CustomSMTPServer(('localhost', 1025), None)

print("Local SMTP server running on port 1025...")
try:
    asyncore.loop()
except KeyboardInterrupt:
    print("Server stopped.")