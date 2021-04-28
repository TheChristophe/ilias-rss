from config_loader import ConfigLoader
from feed_fetcher import FeedFetcher
from mail_sender import MailSender
import schedule
import time


def main():
    config = ConfigLoader('config.ini')
    feed_fetcher = FeedFetcher(config)
    # initial poll to get most recent alert id
    print("Initial fetch to set references...")
    feed_fetcher.poll()

    mail = MailSender(config)

    def job():
        try:
            new_results = feed_fetcher.poll_new()
            new_results.reverse()
            for result in new_results:
                mail.mail_entry(result)
            print(f"Mailing {len(new_results)} entries")
        except FeedFetcher.Inaccessible:
            print('Failed to load feed, deferring to next interval')

    print("Scheduling...")
    schedule.every(config.get_interval()).minutes.do(job)
    print("Now looping!")
    while True:
        schedule.run_pending()
        time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
