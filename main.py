from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from utils.logger import setup_logger
from utils.validator import is_valid_tweet
from utils.twitter_api import post_tweet
from utils.db import get_next_quote, mark_quote_as_used
import logging
import time

executors = {
    'default': ThreadPoolExecutor(1)
}

logger = setup_logger()
scheduler = BackgroundScheduler(executors=executors)

def scheduled_tweet():
    try:
        quote = get_next_quote()
        if not quote:
            logger.warning("No unused quotes available.")
            return

        tweet_text = f"{quote['quote_text']} — {quote['author']}"

        if is_valid_tweet(tweet_text):
            post_tweet(tweet_text)
            mark_quote_as_used(quote['id'])
            logger.info("Tweet posted successfully.")
        else:
            logger.warning("Invalid tweet format, skipped.")
    except Exception as e:
        logger.error(f"Error during scheduled tweet: {e}")

if __name__ == '__main__':
    logger.info("Starting scheduler...")
    scheduler.add_job(scheduled_tweet, 'cron', hour=9, minute=0)
    scheduler.start()

    try:
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler stopped.")
        scheduler.shutdown()
