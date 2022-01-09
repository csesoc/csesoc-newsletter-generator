from airium import Airium
from scrapers.facebook import get_upcoming_events
from scrapers.media import get_articles
from scrapers.opportunities import get_opportunities

from newsletter.styles import LIGHT_GREY
from newsletter.header import add_header
from newsletter.events import add_events
from newsletter.articles import add_articles
from newsletter.opportunities import add_opportunities
from newsletter.footer import add_footer

TABLE_KWARGS = {
    "width": "100%",
    "cellpadding": "0",
    "cellspacing": "0",
}

if __name__ == "__main__":
    facebook_events = get_upcoming_events()
    media_articles = get_articles()
    opportunities = get_opportunities()

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

            # with a.style(type='text/css'):
            #     a('#outlook a {padding: 0;}.ReadMsgBody {width: 100%;}.ExternalClass {width: 100%;}.ExternalClass * {line-height: 100%;}body {margin: 0;padding: 0;-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;}table,td {border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;}img {border: 0;height: auto;line-height: 100%;outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;}p {display: block;margin: 13px 0;}a {text-decoration:none;}')
            # with a.style(type='text/css'):
            #     a('@media only screen and (max-width:480px) {@-ms-viewport {width: 320px;}@viewport {width: 320px;}}')
            # with a.style(type='text/css'):
            #     a('@import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);')
            # with a.style(type='text/css'):
            #     a('@media only screen and (min-width:480px) {.mj-column-px-600 {width: 600px!important;max-width: 600px;}.mj-column-px-500 {width: 500px!important;max-width: 500px;}.mj-column-per-50 {width: 50%!important;max-width: 50%;}.mj-column-per-100 {width: 100%!important;max-width: 100%;}}')
            # with a.style(type='text/css'):
            #     a('@media only screen and (max-width:480px) {table.full-width-mobile {width: 100%!important;}td.full-width-mobile {width: auto!important;}}')
            # with a.style(type='text/css'):
            #     a('@media only screen and (max-width:480px) {.height-fix {height:80px!important;}}')
            # with a.style(type='text/css'):
            #     a('@media only screen and (max-width:480px) {.height-fix-sponsor {height:185px!important;}}')

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

    with open("soc-announce.html", "w") as f:
        f.write(str(a))
