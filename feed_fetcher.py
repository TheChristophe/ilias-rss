from config_loader import ConfigLoader
import urllib.request
import feedparser

class FeedFetcher:
    class Inaccessible(Exception):
        pass

    def __init__(self, config: ConfigLoader):
        self.config = config
        self.auth = urllib.request.HTTPBasicAuthHandler()
        self.entries = []
        self.newest_entry = ''

    def fetch(self, attempt: int = 0) -> feedparser.FeedParserDict:
        if attempt > 2:
            print("stopping fetching")
        opener = urllib.request.build_opener(self.auth)
        try:
            data = opener.open(self.config.get_url())
        except urllib.error.HTTPError as err:
            if err.code != 401 or 'WWW-Authenticate' not in err.headers:
                raise self.Inaccessible()
            # Basic realm="ILIAS Newsfeed"
            realm = err.headers['WWW-Authenticate'].split('"')[1]
            print(realm)
            self.auth.add_password(realm=realm, uri=self.config.get_uri(), user=self.config.get_username(), passwd=self.config.get_password())
            return self.fetch(attempt + 1)
        feed = feedparser.parse(data)
        return feed

    def poll(self):
        feed = self.fetch()
        self.entries = feed['entries']
        self.newest_entry = feed['entries'][0]['id']
        return self.entries

    def poll_new(self):
        feed = self.fetch()
        self.entries = feed['entries']
        newest_entry = feed['entries'][0]['id']
        if newest_entry != self.newest_entry:
            l = []
            for e in self.entries:
                if e['id'] == self.newest_entry:
                    self.newest_entry = newest_entry
                    return l
                else:
                    l.append(e)

        return []
