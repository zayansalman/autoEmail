import smtplib
from credentials import EMAIL, PASSWORD, MAIL_LIST

sent_from = EMAIL #your email address
to = MAIL_LIST #your password
subject = 'Auto Email Test'
body = 'Also test'

email_text = """\
From: %s
To: %s
Subject:%s

%s
""" % (sent_from, ",".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(EMAIL, PASSWORD) #add your email address and password
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print("Email sent successfully!")
except Exception as ex:
    print("Something went wrong...", ex)


