# Python Script to Automate email with attachments and multiple recepeients
import os
import smtplib
from email.message import EmailMessage

email_id = 'sender@gmail.com'  # your email here
email_pass = 'Enter your password here'  # your password here


recipient_list = ['recepient1@gmail.com',
                  'recepient2@gmail.com', 'recepient3@gmail.com']  # recepient emails here
msg = EmailMessage()
msg['Subject'] = 'Enter your Subject line :)' #Email subject line here
msg['From'] = email_id
msg['To'] = recipient_list

msg.set_content('line1\
    line2\ line3\n line4')  # email body text here

for each_file in os.listdir():
    if each_file == 'Script.py':
        continue
    with open(each_file, 'rb') as f:
        file_data = f.read()
        file_name = f.name
        msg.add_attachment(file_data, maintype='application',
                           subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)
