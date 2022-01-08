from newsletter.components import add_button, add_divider, add_section_header
from newsletter.styles import CAPTION, DESC, TITLE

def add_event(a, event):
    with a.table(cellpadding="10").tr():
        with a.td(width="50%", style="vertical-align: top").table():
            with a.tr().td():
                with a.a(href=event.url, target="_blank"):
                    a.img(src=event.img, width="100%", alt=f"Cover photo for {event.title}")
            with a.tr().td().table(cellpadding="5", style=CAPTION):
                with a.tr():
                    a.td(_t="📆")
                    a.td(_t=event.time)
                with a.tr():
                    a.td(_t="📍")
                    a.td(_t=event.location)

        with a.td(width="50%", style="vertical-align: top").table():
            with a.tr().td():
                a.h3(_t=event.title, style=TITLE)
            with a.tr().td():
                a.div(_t=event.description, style=DESC)
            with a.tr().td():
                add_button(a, event.url, "See more")
    #                 with a.tr():
    #                     with a.td(align='center', style='font-size:0px;padding:10px 25px;word-break:break-word;', **{'vertical-align': 'middle'}):
    #                         with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='border-collapse:separate;width:100%;line-height:100%;'):
    #                             with a.tr():
    #                                 with a.td(align='center', bgcolor='#1051ea', role='presentation', style='border:none;border-radius:3px;cursor:auto;padding:4px 25px;background:#1051ea;color:#ffffff;font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;font-weight:normal;Margin:0;text-decoration:none;text-transform:none;', valign='middle'):
    #                                     add_button(a, event.url, "See more")

def add_events(a, events):
    if not events:
        return

    add_section_header(a, "Upcoming Events")
    add_divider(a)
    for event in events:
        add_event(a, event)
        add_divider(a)
