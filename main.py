from config_loader import ConfigLoader
from feed_fetcher import FeedFetcher
from mail_sender import MailSender
import schedule
import time


def main():
    config = ConfigLoader('config.ini')
    feed_fetcher = FeedFetcher(config)
    results = feed_fetcher.poll()
    mail = MailSender(config)
    # mail.mail_entry(results[0])

    def job():
        print('running job')
        new_results = feed_fetcher.poll_new()
        print(new_results)
        for result in new_results.reverse():
            mail.mail_entry(result)

    schedule.every(config.get_interval()).minutes.do(job)
    print('waiting for scheduled jobs')
    while True:
        schedule.run_pending()
        time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
