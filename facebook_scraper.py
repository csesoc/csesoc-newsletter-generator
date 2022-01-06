import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

from classes.event import Event

# Mobile Facebook pages don't rely on JavaScript, making it easier to scrape
CSESOC_EVENTS_PAGE = "https://m.facebook.com/csesoc/events/"

def remove_attrs(soup, whitelist=[]):
    for attr in [attr for attr in soup.attrs if attr not in whitelist]:
        del soup[attr]

    for tag in soup.findAll(True):
        for attr in [attr for attr in tag.attrs if attr not in whitelist]:
            del tag[attr]

def replace_referral_link(a):
    if "lm.facebook.com" not in a["href"]:
        return

    parsed = urlparse(a["href"])
    queries = parse_qs(parsed.query)
    a["href"] = queries["u"][0]

def scrape_event_page(href):
    page = requests.get(f"https://m.facebook.com{href}")
    soup = BeautifulSoup(page.content, "html.parser")

    url = f"https://www.facebook.com{href}"

    title = soup.find_all("h1")[-1].get_text()

    description = soup.find(id="event_tabs").find(text="Details").find_next("div")
    remove_attrs(description, ["href", "target"])
    for a in description.find_all("a"):
        replace_referral_link(a)

    summary = soup.find(id="event_summary").find_all(text=True)
    time = summary[1]
    location = summary[3]

    cover_photo = soup.find(id="event_header").find("img")["src"]

    return Event(url, title, description, time, location, cover_photo)

def get_upcoming_events():
    page = requests.get(CSESOC_EVENTS_PAGE)
    soup = BeautifulSoup(page.content, "html.parser")

    # Assuming all event links should be for upcoming events
    upcoming_events_links = soup.select("a[href*=\/events\/]")
    upcoming_events_details = [scrape_event_page(a["href"]) for a in upcoming_events_links]
    print(upcoming_events_details)

if __name__ == "__main__":
    get_upcoming_events()