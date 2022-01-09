from newsletter.styles import BLUE, BUTTON, DIVIDER, SECTION_HEADER


def add_divider(a):
    a.p(style=DIVIDER)

def add_section_header(a, section_name):
    with a.table(style=SECTION_HEADER, cellpadding="20"):
        with a.tr().td().table():
            with a.tr():
                a.td(_t=section_name, style=f"border-bottom: 5px solid {BLUE}")

def add_button(a, url, text):
    with a.a(href=url, target='_blank'):
        with a.table(style=BUTTON, width="100%", cellpadding="10").tr().td():
            a(text)
