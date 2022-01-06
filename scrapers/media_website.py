import requests
from bs4 import BeautifulSoup

from classes.article import Article

MEDIA_WEBSITE = "https://media.csesoc.org.au"

def scrape_article(article):
    url = f"{MEDIA_WEBSITE}{article.find('a')['href']}"
    title = article.find("h2").get_text()
    description = article.find("p").get_text()
    img = f"{MEDIA_WEBSITE}{article.find('img')['src']}"

    return Article(url, title, description, img)

def get_articles(max=3):
    page = requests.get(MEDIA_WEBSITE)
    soup = BeautifulSoup(page.content, "html.parser")
    articles = soup.find_all("article")[:max]

    return [scrape_article(article) for article in articles]

if __name__ == "__main__":
    get_articles()
