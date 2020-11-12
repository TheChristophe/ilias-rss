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

    def check_sections(self):
        needed_sections = ['Credentials', 'Location']
        for section in needed_sections:
            if section not in self.config:
                raise self.SectionNotFound(section)

    def check_keys(self):
        needed_auth_keys = ['username', 'password']
        needed_connect_keys = ['url']
        for key in needed_auth_keys:
            if key not in self.config['Credentials']:
                raise self.KeyNotFound(key)
        for key in needed_connect_keys:
            if key not in self.config['Location']:
                raise self.KeyNotFound(key)

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_url(self):
        return self.url

    def get_uri(self):
        return self.uri
