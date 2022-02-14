import requests
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


def scrape_event_page(path):
    page = requests.get(f"https://mbasic.facebook.com{path}", headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")

    url = f"https://www.facebook.com{path}"

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


def get_upcoming_events(path="/csesoc/events"):
    page = requests.get(f"{MBASIC_FACEBOOK}{path}", headers=HEADERS)
    soup = BeautifulSoup(page.content, "html.parser")

    # Assuming all event links should be for upcoming events
    upcoming_events_links = soup.select("a[href*=\/events\/]")
    upcoming_events = [scrape_event_page(a["href"].split("?")[0]) for a in upcoming_events_links]

    # Events may be paginated if there are more than 5 upcoming events
    see_more_button = soup.find(id="m_more_friends_who_like_this")
    if see_more_button:
        more_events = get_upcoming_events(see_more_button.find('a')['href'])
        upcoming_events.extend(more_events)

    return upcoming_events


if __name__ == "__main__":
    get_upcoming_events()
