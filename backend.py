# Importing the required modules
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Setting up the email credentials
sender_email = "your_email@gmail.com"
sender_password = "your_password"
receiver_email = "your_receiver_email@gmail.com"

# Creating a Gmail API service instance
service = smtplib.SMTP('smtp.gmail.com', 587)
service.ehlo()
service.starttls()
service.login(sender_email, sender_password)

# Creating a message for the email
subject = "Email Notification System"
message_text = "Hello, this is an email notification system that uses machine learning algorithms to predict which users are most likely to unsubscribe, and sends targeted campaigns to retain them."

# Creating a MIME object
message = MIMEMultipart()
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email

# Attaching the message text
message.attach(MIMEText(message_text))

# Sending the email
service.sendmail(sender_email, receiver_email, message.as_string())
service.quit()

# Printing a confirmation message
print("Email sent successfully!")
