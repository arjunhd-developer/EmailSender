from email.message import EmailMessage
import os
import ssl
import smtplib

email_sender = 'arjunhd.developer@gmail.com'
email_pass = os.environ.get('GOOGLE_APP_PASSWORD')

if email_pass is None:
    raise Exception('Google app password is not set as an environment variable')

email_receiver = 'arjunhd1992@gmail.com'
subject = 'Test mail'
body = '''
This is a very short test email
'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Use the default CA certificates bundle path for macOS
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_pass)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    print('Mail Sent')
