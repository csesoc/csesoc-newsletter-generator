from .styles import DARK_GREY, SOCIALS
from .components import add_section_header


SPONSORS_IMAGE = "https://i.imgur.com/pr09Qdf.jpeg"

LINKS = {
    "Facebook Page": "https://www.facebook.com/csesoc",
    "Facebook Community Group": "https://www.facebook.com/groups/csesoc/",
    "Instagram": "https://www.instagram.com/csesoc_unsw/",
    "TikTok": "https://www.tiktok.com/@csesoc",
    "LinkedIn": "https://www.linkedin.com/company/csesoc",
    "YouTube": "https://www.youtube.com/channel/UC1JHpRrf9j5IKluzXhprUJg/",
    "Discord": "https://bit.ly/CSESocDiscord",
}


def add_links(a):
    """Formats links in the format LINK | LINK | LINK"""

    for i, (name, link) in enumerate(LINKS.items()):
        a.a(href=link, target="_blank", _t=name, style=f"color: {DARK_GREY}")

        if i != len(LINKS) - 1:
            a("|")


def add_sponsors(a):
    with a.tr().th(colspan="2", style="text-align: center;"):
        add_section_header(a, "Sponsors")
    with a.tr().td(colspan="2"):
        a.div(
            style=f"background: url({SPONSORS_IMAGE}) bottom center / contain no-repeat; height: 850px;"
        )


def add_socials(a):
    with a.table(align="center", style=SOCIALS, cellpadding="30"):
        with a.tr().td().table(cellpadding="10"):
            with a.tr().td():
                add_links(a)

            with a.tr().td():
                a("Contact:")
                a.a(
                    href="mailto:info@csesoc.org.au",
                    target="_blank",
                    _t="info@csesoc.org.au",
                    style=f"color: {DARK_GREY}; font-weight: bold;",
                )

            with a.tr().td():
                a(
                    "As a student of the School of Computer Science and Engineering you receive the CSESoc newsletter. If you do not wish to receive our newsletters,"
                )
                a.a(
                    href="https://status.cse.unsw.edu.au/Control_Panel/Mail/Mailing_List_Subscriptions/",
                    target="_blank",
                    _t="unsubscribe here",
                    style=f"color:{DARK_GREY}; font-weight: bold;",
                )

            with a.tr().td():
                a.i(_t="Copyright © 2025 CSESoc UNSW. All rights reserved.")


def add_footer(a):
    add_sponsors(a)
    add_socials(a)
