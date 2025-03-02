import sys
from airium import Airium

from scrapers.facebook import get_upcoming_events, man_get_upcoming_events
from scrapers.media import get_articles, man_get_articles
from scrapers.opportunities import get_opportunities, man_get_opportunities

from newsletter.styles import LIGHT_GREY
from newsletter.header import add_header
from newsletter.events import add_events
from newsletter.articles import add_articles
from newsletter.opportunities import add_opportunities
from newsletter.footer import add_footer
from newsletter.gui import launch_gui

TABLE_KWARGS = {
    "width": "100%",
    "cellpadding": "0",
    "cellspacing": "0",
}

CMD_OPTIONS = {'-m', '-a', '-gui'}

VALID_CMD_LEN = {1, 2}

def generate_newsletter(facebook_events, media_articles, opportunities, save_file=True):
    a = Airium()
    a("<!DOCTYPE html>")
    with a.html(
        xmlns="http://www.w3.org/1999/xhtml",
        **{
            "xmlns:o": "urn:schemas-microsoft-com:office:office",
            "xmlns:v": "urn:schemas-microsoft-com:vml",
        },
    ):

        # Some email clients strip away the `<head>`, so sometimes fonts and stylesheets won't get loaded.
        # Try to use inline styling instead of relying on styling in `<head>`
        with a.head():
            a.title(_t="soc-announce")
            a.meta(content="IE=edge", **{"http-equiv": "X-UA-Compatible"})
            a.meta(content="text/html; charset=UTF-8", **{"http-equiv": "Content-Type"})
            a.meta(content="width=device-width, initial-scale=1", name="viewport")

            # Fonts
            a.link(
                href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700",
                rel="stylesheet",
                type="text/css",
            )
            a.link(
                href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap",
                rel="stylesheet",
                type="text/css",
            )

        # Nesting content in at least two tables deep is best practice
        with a.body().table(id="bodyTable", width="100%"):
            with a.tr().td(align="center").table(
                id="emailContainer",
                width="800",
                cellpadding="50",
                cellspacing="0",
                style=f"background: {LIGHT_GREY};",
            ):
                with a.tr().td().table(
                    id="emailContent",
                    width="700",
                    cellpadding="0",
                    cellspacing="0",
                    style="background: white;",
                ):
                    with a.thead():
                        with a.tr().td().table(id="emailHeader", **TABLE_KWARGS):
                            with a.tr().td():
                                add_header(a)
                    with a.tbody():
                        with a.tr().td().table(id="emailBody", **TABLE_KWARGS):
                            with a.tr().td().table(id="upcomingEvents", **TABLE_KWARGS):
                                with a.tr().td():
                                    add_events(a, facebook_events)
                            with a.tr().td().table(id="mediaArticles", **TABLE_KWARGS):
                                with a.tr().td():
                                    add_articles(a, media_articles)
                            with a.tr().td().table(id="opportunities", **TABLE_KWARGS):
                                with a.tr().td():
                                    add_opportunities(a, opportunities)
                    with a.tfoot():
                        with a.tr().td().table(id="emailFooter", **TABLE_KWARGS):
                            with a.tr().td():
                                add_footer(a)

    if save_file:
        with open("soc-announce.html", "w") as f:
            f.write(str(a))
        return "soc-announce.html"

    return str(a)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py [-m | -a | -gui]")
        sys.exit(1)
        
    if sys.argv[1] not in CMD_OPTIONS:
        print("Usage: python3 main.py [-m | -a | -gui]")
        sys.exit(1)

    if sys.argv[1] == '-gui':
        launch_gui()
    elif sys.argv[1] == '-m':
        facebook_events = man_get_upcoming_events()
        media_articles = man_get_articles()
        opportunities = man_get_opportunities()
        generate_newsletter(facebook_events, media_articles, opportunities)
    elif sys.argv[1] == '-a':
        # Default to -a
        facebook_events = get_upcoming_events()
        media_articles = get_articles()
        opportunities = get_opportunities()
        generate_newsletter(facebook_events, media_articles, opportunities)
