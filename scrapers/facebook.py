import os
import re
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

from scrapers.helpers import remove_attrs

# Mobile Facebook pages don't use JavaScript, making it easier to scrape
MBASIC_FACEBOOK = "https://mbasic.facebook.com"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}


class Event:
    def __init__(self, url, title, description, time, location, img):
        self.url = url
        self.title = title
        self.description = description
        self.time = time
        self.location = location
        self.img = img


def replace_referral_link(a):
    if "lm.facebook.com" not in a["href"]:
        return

    parsed = urlparse(a["href"])
    queries = parse_qs(parsed.query)
    a["href"] = queries["u"][0]


def format_event_time(event_time):
    # Remove timezones in string (it's gonna be Sydney)
    event_time = re.sub(r" UTC\+\d+", "", event_time)

    # Convert all 24-hour times to 12-hour times
    matches = re.findall(r"((2[0-3]|[01]?[0-9]):([0-5]?[0-9]))", event_time)
    for match in matches:
        time = match[0]
        d = datetime.strptime(time, "%H:%M")
        event_time = event_time.replace(time, d.strftime("%-I:%M %p"))

    return event_time


def get_event_id(contents):
    url = re.search("<!-- saved from url=.*-->", contents)
    return url.group().split('/')[-2]


def scrape_event_page(contents):
    soup = BeautifulSoup(contents, "html.parser")
    url = f"https://www.facebook.com/events/{get_event_id(contents)}"

    title = soup.find("header").find("h1").get_text()
    print(title)

    description = soup.find(id="event_tabs").find("section")
    remove_attrs(description)
    for a in description.find_all("a"):
        replace_referral_link(a)

    summary = soup.find(id="event_summary").find_all("table")
    time = format_event_time(summary[0].find("div").text)

    # location is sometimes optional
    try:
        location = summary[1].find("div").text
    except:
        location = None

    img = soup.find(id="event_header").find("img")["src"]

    return Event(url, title, description, time, location, img)


def get_upcoming_events():
    directory = os.path.dirname(os.path.abspath(__file__))
    cached_pages = os.path.join(directory, 'cached_pages')
    upcoming_events = []

    for filename in os.listdir(cached_pages):
        if filename.endswith('.html'):
            filename = os.path.join(cached_pages,filename)

            with open(filename, 'r') as f:
                event_page = scrape_event_page(f.read())
                upcoming_events.append(event_page)

    return upcoming_events


if __name__ == "__main__":
    get_upcoming_events()
