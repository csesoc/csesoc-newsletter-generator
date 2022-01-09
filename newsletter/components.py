from newsletter.styles import BUTTON, DIVIDER, SECTION_HEADER

def add_divider(a):
    a.p(style=DIVIDER)

def add_section_header(a, section_name):
    with a.table(cellpadding="20", style="margin-left: auto; margin-right: auto;"):
        with a.tr().td().table():
            with a.tr().td():
                a.h2(_t=section_name, style=SECTION_HEADER)

def add_button(a, url, text):
    with a.a(href=url, target='_blank'):
        with a.table(style=BUTTON, width="100%", cellpadding="10").tr().td():
            a(text)
