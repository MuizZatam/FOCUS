import smtpd
import asyncore


class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, mailfrom, rcpttos, data):
        print(f"Received email from: {mailfrom}")
        print(f"Recipients: {rcpttos}")
        print(f"Data: {data}")

server = CustomSMTPServer(('localhost', 1025), None)


def main():
    asyncore.loop()
