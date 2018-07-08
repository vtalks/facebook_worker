import sys
import time
import logging

import schedule
import requests


def job():
    logging.info("Get a random talk ...")
    # get a random talk
    r = requests.get('https://vtalks.net/api/talk/random-talk/')
    if r.status_code != 200:
        logging.error("Can't fetch a random talk, response status code is", r.status_code)
        exit(1)

    talk_json = r.json()

    logging.debug(talk_json)

    page_id = "2014044952145721"
    access_token = "2014044952145721|dcgMRZ5624yP3__GwDkBEVZhvSc"
    url = "https://graph.facebook.com/{:s}/feed?message=test&access_token={:s}".format(page_id, access_token)
    result = requests.post(url)
    print(result.text)


def main(argv):
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Starting facebook-worker ...')

    job()
    exit(0)

    schedule.every(6).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main(sys.argv[1:])
