'''
import smtplib, ssl
def sendemail(receiver,content):
  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  sender_email = "group4python@gmail.com"  
  password =("mihallaris")
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver, content)
'''