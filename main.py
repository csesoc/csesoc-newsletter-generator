from airium import Airium
from scrapers.facebook import get_upcoming_events
from scrapers.media import get_articles
from scrapers.opportunities import get_opportunities

from newsletter.header import add_header
from newsletter.events import add_events
from newsletter.articles import add_articles
from newsletter.opportunities import add_opportunities
from newsletter.footer import add_footer

if __name__ == "__main__":
    facebook_events = get_upcoming_events()
    media_articles = get_articles()
    opportunities = get_opportunities()

    a = Airium()
    a('<!DOCTYPE html>')
    with a.html(xmlns='http://www.w3.org/1999/xhtml', **{'xmlns:o': 'urn:schemas-microsoft-com:office:office',
 'xmlns:v': 'urn:schemas-microsoft-com:vml'}):
        with a.head():
            a.title(_t="soc-announce")
            a.meta(content='IE=edge', **{'http-equiv': 'X-UA-Compatible'})
            a.meta(content='text/html; charset=UTF-8', **{'http-equiv': 'Content-Type'})
            a.meta(content='width=device-width, initial-scale=1', name='viewport')
            a.link(href='https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700', rel='stylesheet', type='text/css')
            with a.style(type='text/css'):
                a('#outlook a {padding: 0;}.ReadMsgBody {width: 100%;}.ExternalClass {width: 100%;}.ExternalClass * {line-height: 100%;}body {margin: 0;padding: 0;-webkit-text-size-adjust: 100%;-ms-text-size-adjust: 100%;}table,td {border-collapse: collapse;mso-table-lspace: 0pt;mso-table-rspace: 0pt;}img {border: 0;height: auto;line-height: 100%;outline: none;text-decoration: none;-ms-interpolation-mode: bicubic;}p {display: block;margin: 13px 0;}a {text-decoration:none;}')
            with a.style(type='text/css'):
                a('@media only screen and (max-width:480px) {@-ms-viewport {width: 320px;}@viewport {width: 320px;}}')
            with a.style(type='text/css'):
                a('@import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);')
            with a.style(type='text/css'):
                a('@media only screen and (min-width:480px) {.mj-column-px-600 {width: 600px!important;max-width: 600px;}.mj-column-px-500 {width: 500px!important;max-width: 500px;}.mj-column-per-50 {width: 50%!important;max-width: 50%;}.mj-column-per-100 {width: 100%!important;max-width: 100%;}}')
            with a.style(type='text/css'):
                a('@media only screen and (max-width:480px) {table.full-width-mobile {width: 100%!important;}td.full-width-mobile {width: auto!important;}}')
            with a.style(type='text/css'):
                a('@media only screen and (max-width:480px) {.height-fix {height:80px!important;}}')
            with a.style(type='text/css'):
                a('@media only screen and (max-width:480px) {.height-fix-sponsor {height:185px!important;}}')

        # nesting content in at least two tables deep is best practice
        with a.body().table(id="bodyTable", border="0", cellpadding="0", cellspacing="0", height="100%", width="100%").tr().td(align="center", valign="top").table(id="emailContainer", border="0", cellpadding="20", cellspacing="0", width="800"):
            with a.thead().tr().td(align="center", valign="top").table(id="emailHeader", border="0", cellpadding="20", cellspacing="0", width="100%").tr().td(align="center", valign="top"):
                add_header(a)
            with a.body().tr().td(align="center", valign="top").table(id="emailBody", border="0", cellpadding="20", cellspacing="0", width="100%"):

                if facebook_events:
                    with a.tr().td(align="center", valign="top").table(id="upcomingEvents", border="0", cellpadding="20", cellspacing="0", width="100%").tr().td(align="center", valign="top"):
                        add_events(a, facebook_events)

                if media_articles:
                    with a.tr().td(align="center", valign="top").table(id="mediaArticles", border="0", cellpadding="20", cellspacing="0", width="100%").tr().td(align="center", valign="top"):
                        add_articles(a, media_articles)

                if opportunities:
                    with a.tr().td(align="center", valign="top").table(id="opportunities", border="0", cellpadding="20", cellspacing="0", width="100%").tr().td(align="center", valign="top"):
                        add_opportunities(a, opportunities)

            with a.tfoot().tr().td(align="center", valign="top").table(id="emailFooter", border="0", cellpadding="20", cellspacing="0", width="100%").tr().td(align="center", valign="top"):
                add_footer(a)

    with open("soc-announce.html", "w") as f:
        f.write(str(a))
