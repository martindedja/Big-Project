import smtplib, ssl
port = 465  # For SSL
midhi="midhi"
smtp_server = "smtp.gmail.com"
sender_email = "group4python@gmail.com"  
receiver_email = "stefanomihallari@gmail.com" 
password =("mihallaris")
message = """\
Subject: You have resetted your Billing System password.

Your new password is {}""".format(midhi)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)