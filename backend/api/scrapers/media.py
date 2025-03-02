import requests
from bs4 import BeautifulSoup

from .helpers import input_sanitise

MEDIA_WEBSITE = "https://media.csesoc.org.au"


class Article:
    def __init__(self, url, title, description, img):
        self.url = url
        self.title = title
        self.description = description
        self.img = img


def scrape_article(article):
    url = f"{MEDIA_WEBSITE}{article.find('a')['href']}"
    title = article.find("h2").get_text()
    description = article.find("div").get_text()
    if article.find("img") is None:
        img = None
    else:
        img = f"{MEDIA_WEBSITE}{article.find('img')['src']}"
    return Article(url, title, description, img)


def get_articles(max=3):
    page = requests.get(MEDIA_WEBSITE)
    soup = BeautifulSoup(page.content, "html.parser")
    articles = soup.find_all("article")[:max]

    return [scrape_article(article) for article in articles]


def man_get_articles():
    medias = []

    line = input_sanitise("Add new media? [y/n]: ", {"y", "n"})

    while line == "y":
        url = input_sanitise("Enter media URL: ")
        title = input_sanitise("Enter media title: ")
        description = input_sanitise("Enter media description: ")
        img = input_sanitise("Enter media image URL: ")

        medias.append(Article(url, title, description, img))

        line = input_sanitise("Add new media? [y/n]: ", {"y", "n"})

    return medias


if __name__ == "__main__":
    articles = get_articles()

    for article in articles:
        print("URL:  ", article.url)
        print("TITLE:", article.title)
        print("IMG:  ", article.img)
        print("DESC: ", article.description)
        print()
