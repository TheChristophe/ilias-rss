from config_loader import ConfigLoader
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
import jinja2


class MailSender:
    def __init__(self, config: ConfigLoader):
        self.config = config
        self.smtp = smtplib.SMTP(config.get_mail_host())
        self.smtp.starttls()
        self.smtp.login(config.get_mail_username(), config.get_mail_password())
        self.jinja = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))

    def _new_mail(self, subject: str):
        multipart = MIMEMultipart()
        multipart['From'] = formataddr(('Notification service', self.config.get_mail_from()))
        multipart['To'] = self.config.get_mail_to()
        multipart['Subject'] = subject
        return multipart

    def send_mail(self, message: str, subject: str = 'Notification'):
        multipart = self._new_mail(subject)

        multipart.attach(MIMEText(message, 'plain'))
        self.smtp.send_message(multipart)

    def send_mail_html(self, html_message: str, subject: str = 'Notification'):
        multipart = self._new_mail(subject)

        multipart.attach(MIMEText(html_message, 'html'))
        self.smtp.send_message(multipart)

    def mail_entry(self, entry: dict):
        title = entry['title']
        link = entry['links'][0]['href']
        body = entry['summary_detail']['value']
        template = self.jinja.get_template('email.html.jinja')
        text = template.render(title=title, link=link, body=body)
        self.send_mail_html(text, title)
