from newsletter.components import add_button, add_divider, add_section_header
from newsletter.helpers import convert_to_id
from newsletter.styles import CAPTION, DESC, TITLE


def add_event(a, event):
    with a.td(width="45%", style="vertical-align: top").table(style="width: 100%"):
        with a.tr().td():
            with a.a(href=event.url, target="_blank"):
                a.img(src=event.img, width="100%", alt=f"Cover photo for {event.title}")
        with a.tr().td().table(cellpadding="5", style=CAPTION):
            with a.tr():
                a.td(_t="📆")
                a.td(_t=event.time)

            if event.location:
                with a.tr():
                    a.td(_t="📍")
                    a.td(_t=event.location)

    with a.td(width="55%", style="vertical-align: top").table(style="width: 100%"):
        with a.tr().td():
            a.h3(_t=event.title, style=TITLE)
        with a.tr().td():
            a.div(_t=event.description, style=DESC)
        with a.tr().td():
            add_button(a, event.url, "See more")


def add_events(a, events):
    if not events:
        return

    with a.table(cellpadding="10"):
        with a.tr().th(colspan="2", style="text-align: center;"):
            add_section_header(a, "Events")
        with a.tr().td(colspan="2"):
            add_divider(a)

        for event in events:
            if not event:
                continue
            with a.tr(id=convert_to_id(event.title)):
                add_event(a, event)
            with a.tr().td(colspan="2"):
                add_divider(a)
