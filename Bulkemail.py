import pandas as pd
import smtplib

SenderAddress = "<Email Address of sender>"
password = "password of sender"

e = pd.read_excel("email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("abhikumarx0x@gmail.com","panjikar@12345")
msg = "Hello Mohit Panjikar this side, i am testing bulk email service !!!"
subject = "Bulk email service"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail("abhikumarx0x@gmail.com", email, body)
server.quit()
