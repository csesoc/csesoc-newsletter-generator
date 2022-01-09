from newsletter.components import add_button, add_divider, add_section_header
from newsletter.styles import DESC, TITLE

def add_article(a, article):
    with a.table(cellpadding="10").tr():
        with a.td(width="45%", style="vertical-align: top").table():
            with a.tr().td():
                with a.a(href=article.url, target="_blank"):
                    a.img(src=article.img, width="100%", alt=f"Cover photo for {article.title}")

        with a.td(width="55%", style="vertical-align: top").table():
            with a.tr().td():
                a.h3(_t=article.title, style=TITLE)
            with a.tr().td():
                a.div(_t=article.description, style=DESC)
            with a.tr().td():
                add_button(a, article.url, "Read more")

def add_articles(a, articles):
    if not articles:
        return

    add_section_header(a, "Media")
    add_divider(a)
    for article in articles:
        add_article(a, article)
        add_divider(a)
