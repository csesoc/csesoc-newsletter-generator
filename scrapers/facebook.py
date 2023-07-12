import os
import requests
import re
import time
import mechanicalsoup
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv


from scrapers.helpers import remove_attrs, HEADERS

# Mobile Facebook pages don't use JavaScript, making it easier to scrape
MBASIC_FACEBOOK = "https://mbasic.facebook.com"



class Event:
    def __init__(self, url, title, description, time, location, img):
        self.url = url
        self.title = title
        self.description = description
        self.time = time
        self.location = location
        self.img = img


def login(url):

    # load environment variables
    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")

    browser = mechanicalsoup.StatefulBrowser()

    # check if string begins with https://mbasic.facebook.com
    if re.match(r"^https:\/\/mbasic\.facebook\.com", url) is not None:
        browser.set_user_agent(HEADERS["fireFox"])
    else:
        browser.set_user_agent(HEADERS["iPad"])
   
    # login
    browser.open(url)
    login_form = browser.select_form('form')
    login_form.set("email", username)
    login_form.set("pass", password)


    browser.submit_selected()

    return str(browser.get_current_page())


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


def scrape_event_page(event_id):

    page = login(f"{MBASIC_FACEBOOK}/events/{event_id}")

    # convert page to string
    page = str(page)

    if page is None:
        return None

    soup = BeautifulSoup(page,"html.parser")

    url = f"https://www.facebook.com/events/{event_id}"

    if soup.find("header") is None:
        return None
    
    title = soup.find("title").get_text()

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

    print(title)

    return Event(url, title, description, time, location, img)


def scrape_events(contents):
    soup = BeautifulSoup(contents, "html.parser")

    events = soup.find("div", class_="_51lk").find_all("div", class_="item _1zq- tall acw")
    links = [event.find("a") for event in events]
    hrefs = list(set([l["href"] for l in links if l["href"] != "https://www.facebook.com/csesoc"]))
    event_ids = [href.split('/')[-1] for href in hrefs]

    # remove ?id= from event_ids
    event_ids = [event_id.split('?id=')[-1] for event_id in event_ids]

    return [scrape_event_page(event_id) for event_id in event_ids]


def get_upcoming_events():
    # Link to CSESoc events page on ipad
    url = "https://m.facebook.com/timeline/app_collection/?collection_token=100056988625965%3A2344061033%3A211&paipv=0&eav=AfZ3iHdiQBe4J8DQVdA1R_Cw2ZMZB-30B-mie9hIRyUkZ5YVb14n6N8lzCrQT1JBc7k"
    page = login(url)
    return scrape_events(page)
 



if __name__ == "__main__":
    get_upcoming_events()
