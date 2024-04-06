import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, subject, header, letter_content, footer, smtp_server, smtp_port):
    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Combine header, letter content, and footer
    email_content = f"{header}\n\n{letter_content}\n\n{footer}"

    # Add email content
    message.attach(MIMEText(email_content, "plain"))

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login()
        server.sendmail(sender_email, receiver_email, message.as_string())

# Example usage
