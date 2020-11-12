import configparser
import urllib.parse


class ConfigLoader:
    class SectionNotFound(Exception):
        pass

    class KeyNotFound(Exception):
        pass

    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.config.read(file)
        self.check_sections()
        self.check_keys()

        self.username = self.config['Credentials']['username']
        self.password = self.config['Credentials']['password']

        self.url = self.config['Location']['url']
        self.uri = urllib.parse.urlparse(self.url).netloc

        self.mail_host = self.config['Mail']['host']
        self.mail_port = int(self.config['Mail']['port'])
        self.mail_username = self.config['Mail']['username']
        self.mail_password = self.config['Mail']['password']
        self.mail_from = self.config['Mail']['from']
        self.mail_to = self.config['Mail']['to']

        self.interval = int(self.config['Misc']['interval'])

    def check_sections(self):
        needed_sections = ['Credentials', 'Location', 'Mail', 'Misc']
        for section in needed_sections:
            if section not in self.config:
                raise self.SectionNotFound(section)

    def check_keys(self):
        needed_auth_keys = ['username', 'password']
        needed_connect_keys = ['url']
        needed_mail_keys = ['username', 'password', 'from', 'to', 'host', 'port']
        needed_misc_keys = ['interval']
        for key in needed_auth_keys:
            if key not in self.config['Credentials']:
                raise self.KeyNotFound(key)
        for key in needed_connect_keys:
            if key not in self.config['Location']:
                raise self.KeyNotFound(key)
        for key in needed_mail_keys:
            if key not in self.config['Mail']:
                raise self.KeyNotFound(key)
        for key in needed_misc_keys:
            if key not in self.config['Misc']:
                raise self.KeyNotFound(key)

    def get_username(self) -> str:
        return self.username

    def get_password(self) -> str:
        return self.password

    def get_url(self) -> str:
        return self.url

    def get_uri(self) -> str:
        return self.uri

    def get_mail_host(self) -> str:
        return self.mail_host

    def get_mail_port(self) -> int:
        return self.mail_port

    def get_mail_username(self) -> str:
        return self.mail_username

    def get_mail_password(self) -> str:
        return self.mail_password

    def get_mail_from(self) -> str:
        return self.mail_from

    def get_mail_to(self) -> str:
        return self.mail_to

    def get_interval(self) -> int:
        return self.interval
