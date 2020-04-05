import smtplib

class Send_Email():
    def __init__(self):
        self.sender = 'hisabkitab60@gmail.com'
        self.passwd = "hisabkitab2020"

    def send_mail(self, receivers,username,message):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(self.sender, self.passwd)
        server.sendmail(self.sender, receivers, message)
        server.quit()
#receivers = '18bce208@nirmauni.ac.in'


# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, receivers, message)
#    print ("Successfully sent email")
# except Exception:
#    print ("Error: unable to send email")
