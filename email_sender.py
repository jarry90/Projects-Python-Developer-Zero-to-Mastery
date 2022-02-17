import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'name'
email['to'] = 'email@website.com'
email['subject'] = 'subject'

email.set_content('This is the contents of an email.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('email@gmail.com', 'password')
	smtp.send_message(email)
	print('Email sent!')