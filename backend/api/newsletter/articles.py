from newsletter.components import add_button, add_divider, add_section_header
from newsletter.styles import DESC, TITLE
import re

def convert_to_id(name):
    id = name.strip()
    id = re.sub(r"[^\w\s]", '', name)
    id = re.sub(r"\s+", '-', name)
    return id


def add_article(a, article):
    with a.td(width="45%", style="vertical-align: top").table(style="width: 100%"):
        with a.tr().td():
            with a.a(href=article.url, target="_blank"):
                a.img(
                    src=article.img,
                    width="100%",
                    alt=f"Cover photo for {article.title}",
                )

    with a.td(width="55%", style="vertical-align: top").table(style="width: 100%"):
        with a.tr().td():
            a.h3(_t=article.title, style=TITLE)
        with a.tr().td():
            a.div(_t=article.description, style=DESC)
        with a.tr().td():
            add_button(a, article.url, "Read more")


def add_articles(a, articles):
    if not articles:
        return

    with a.table(cellpadding="10"):
        with a.tr().th(colspan="2", style="text-align: center;"):
            add_section_header(a, "Media")
        with a.tr().td(colspan="2"):
            add_divider(a)

        for article in articles:
            with a.tr(id=convert_to_id(article.title)):
                add_article(a, article)
            with a.tr().td(colspan="2"):
                add_divider(a)
