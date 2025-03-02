from .styles import BLUE, DESC, TITLE
from .components import add_divider, add_section_header
import re

def convert_to_id(name):
    id = name.strip()
    id = re.sub(r"[^\w\s]", '', name)
    id = re.sub(r"\s+", '-', name)
    return id


OPPORTUNITIES_HEADER_IMG = "https://i.imgur.com/twzB46W.jpeg"


def add_opportunities_section_header(a):
    a.div(
        style=f"background: url({OPPORTUNITIES_HEADER_IMG}) center center / contain no-repeat; height: 170px;"
    )


def add_opportunity(a, opportunity):
    with a.tr(id=convert_to_id(opportunity.title)).td().table(cellpadding="10", style=f"border-left: 5px solid {BLUE};"):
        with a.tr().td().table():
            a.tr().td().h3(_t=opportunity.title, style=TITLE)
            a.tr().td().div(_t=opportunity.description, style=DESC)


def add_opportunities(a, opportunities):
    if not opportunities:
        return

    with a.table(cellspacing="0", cellpadding="0"):
        with a.tr().th(colspan="2", style="text-align: center;"):
            # add_opportunities_section_header(a)
            add_section_header(a, "Opportunities")
        with a.tr().td(colspan="2"):
            add_divider(a)

        with a.tr().td().table(cellpadding="20"):
            for opportunity in opportunities:
                add_opportunity(a, opportunity)
