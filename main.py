from config_loader import ConfigLoader
from feed_fetcher import FeedFetcher


def main():
    print("main")
    config = ConfigLoader('config.ini')
    feed_fetcher = FeedFetcher(config)
    results = feed_fetcher.poll()
    print(results)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
