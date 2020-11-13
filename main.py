from config_loader import ConfigLoader
from feed_fetcher import FeedFetcher
from mail_sender import MailSender
import schedule
import time


def main():
    config = ConfigLoader('config.ini')
    feed_fetcher = FeedFetcher(config)
    # initial poll to get most recent alert id
    feed_fetcher.poll()

    mail = MailSender(config)

    def job():
        new_results = feed_fetcher.poll_new()
        new_results.reverse()
        for result in new_results:
            mail.mail_entry(result)

    schedule.every(config.get_interval()).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
