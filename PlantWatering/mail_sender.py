import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from device import Device


class MailSender(Device):

    def is_alive(self):
        pass

    def __init__(self):
        super(MailSender, self).__init__(__name__)

    def send_mail(self, to_send):
        msg = MIMEMultipart()
        msg['Subject'] = self.cfg.subject
        msg['From'] = self.cfg.frm
        msg['To'] = self.cfg.to
        message = MIMEText(to_send)
        msg.attach(message)
        try:
            s = smtplib.SMTP('smtp.gmail.com:587')
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(self.cfg.userName, self.cfg.password)
            s.sendmail(self.cfg.frm, self.cfg.to, msg.as_string())
            s.quit()
            self.logger.info('Success : Mail sent!')

        except Exception as e:
            self.logger.error('Failed to send the mail! \n {}'.format(e))