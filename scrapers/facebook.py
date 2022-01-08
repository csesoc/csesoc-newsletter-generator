import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

from scrapers.helpers import remove_attrs

# Mobile Facebook pages don't use JavaScript, making it easier to scrape
CSESOC_EVENTS_PAGE = "https://m.facebook.com/csesoc/events/"

class Event:
    def __init__(self, url, title, description, time, location, img):
        self.url = url
        self.title = title
        self.description = description
        self.time = time
        self.location = location
        self.img = img

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

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

def scrape_event_page(href):
    page = requests.get(f"https://m.facebook.com{href}")
    soup = BeautifulSoup(page.content, "html.parser")

    url = f"https://www.facebook.com{href}"

    title = soup.find_all("h1")[-1].get_text()

    description = soup.find(id="event_tabs").find(text="Details").find_next("div")
    remove_attrs(description)
    for a in description.find_all("a"):
        replace_referral_link(a)

    summary = soup.find(id="event_summary").find_all(text=True)
    time = format_event_time(summary[1])
    location = summary[3]

    img = soup.find(id="event_header").find("img")["src"]

    return Event(url, title, description, time, location, img)

def get_upcoming_events():
    page = requests.get(CSESOC_EVENTS_PAGE)
    soup = BeautifulSoup(page.content, "html.parser")

    # Assuming all event links should be for upcoming events
    upcoming_events_links = soup.select("a[href*=\/events\/]")
    upcoming_events_links.reverse()
    return [scrape_event_page(a["href"]) for a in upcoming_events_links]

if __name__ == "__main__":
    get_upcoming_events()
