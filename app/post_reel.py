import os
import schedule
import time
import logging
from instagrapi import Client

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='reel_poster.log'
)

DAY_COUNT_FILE = 'day_count.txt'

def get_current_day():
    try:
        with open(DAY_COUNT_FILE, 'r') as file:
            day = int(file.read().strip())
    except FileNotFoundError:
        day = 1
    return day

def increment_day(day):
    with open(DAY_COUNT_FILE, 'w') as file:
        file.write(str(day + 1))

def post_reel():
    logging.info("Attempting to post reel...")

    cl = Client()
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    video_path = 'PATH/TO/YOUR/VIDEO.mp4'

    day = get_current_day()
    caption = f"Day {day}\n\nADD_TAGS_HERE"

    try:
        logging.info("Logging in...")
        cl.login(username, password)
        logging.info("Login successful. Uploading video...")
        cl.video_upload(video_path, caption)
        logging.info(f"Reel for Day {day} posted successfully!")
        increment_day(day)
    except Exception as e:
        logging.error(f"Failed to post reel for Day {day}: {e}")

schedule.every().day.at("08:00").do(post_reel)

logging.info("Running! Waiting to post reel at 08:00 AM daily...")

while True:
    schedule.run_pending()
    time.sleep(1)