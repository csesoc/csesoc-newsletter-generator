from newsletter.styles import BLUE, DESC, TITLE


OPPORTUNITIES_HEADER_IMG = "https://i.imgur.com/twzB46W.jpeg"

def add_opportunities_section_header(a):
    a.div(style=f'background: url({OPPORTUNITIES_HEADER_IMG}) center center / contain no-repeat; height: 150px;')

def add_opportunity(a, opportunity):
    with a.table(cellpadding="50").tr():
        with a.td():
            a.div(style=f"height: 100%; width: 100%; border-left: 5px solid {BLUE}", _t=" ")
            # a("test")

        with a.td(width="95%", style="vertical-align: top").table():
            with a.tr().td():
                a.h3(_t=opportunity.title, style=TITLE)
            with a.tr().td():
                a.div(_t=opportunity.description, style=DESC)

    # with a.table(cellpadding="10"):
    #     with a.tr().td().table():
    #             with a.tr().td(style=TITLE):
    #                 a(opportunity.title)
    #             with a.tr().td(style=DESC):
    #                 a(opportunity.description)
    # with a.table(align='center', cellpadding='10', style='margin: 0px auto; min-width: 100%;', width='100%'):
        # with a.tr().td():

            # with a.td(align='center', bgcolor='#1051ea', style='background-color: #1051ea;', valign='top'):
            #     with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='min-width: 100%; margin: 0px auto;mso-table-lspace:0pt; mso-table-rspace:0pt;', width='5'):
            #         with a.tbody():
            #             with a.tr():
            #                 a.td(height='1', style='height: 1px; font-size: 0px; line-height: 0;', valign='top', **{'aria-hidden': 'true'})
            # with a.td(align='center', valign='top'):
            #     with a.table(align='left', border='0', cellpadding='0', cellspacing='0', role='presentation', style='min-width:100%; max-width:100%;mso-table-lspace:0pt; mso-table-rspace:0pt;', width='20'):
            #         with a.tbody():
            #             with a.tr():
            #                 a.td(align='center', height='20', style='height: 20px; font-size: 0px; line-height: 0;', valign='top', **{'aria-hidden': 'true'})
            # with a.td(align='center', valign='top'):
            #     with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='margin: 0px auto; min-width: 100%;', width='100%'):
            #         with a.tbody():
            #             with a.tr():
            #                 with a.td(align='center', valign='top'):
            #                     with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='margin: 0px auto; min-width: 100%;', width='100%'):
            #                         with a.tbody():
            #                             with a.tr():
            #                                 with a.td(align='left', style="font-size: 18px; color: #333333; font-weight: bold; font-family: 'Open Sans', Arial, Helvetica, sans-serif; word-break: break-word; line-height: 1;"):
            #                                     with a.span(style="color: #333333; font-style: normal; text-align: left; line-height: 24px; font-size: 18px; font-weight: 700; font-family: 'Open Sans', Arial, Helvetica, sans-serif;"):
            #                                         with a.strong(style="font-size: 18px; font-weight: 700; font-family: 'Open Sans', Arial, Helvetica, sans-serif;"):
            #                                             a(opportunity.title)
            #                             a('<!-- start space -->')
            #                             with a.tr():
            #                                 a.td(height='7', style='height: 7px; font-size: 0px; line-height: 0;', valign='top', **{'aria-hidden': 'true'})
            #                             a('<!-- end space -->')
            #                             with a.tr():
            #                                 with a.td(align='left', style="font-size: 14px; color: #888888; font-weight: normal; font-family: 'Open Sans', Arial, Helvetica, sans-serif; word-break: break-word; line-height: 1;"):
            #                                     with a.span(style="font-style: normal; text-align: left; color: #888888; line-height: 24px; font-size: 14px; font-weight: 400; font-family: 'Open Sans', Arial, Helvetica, sans-serif;"):
            #                                         a(opportunity.description)
            #                             a('<!-- start space -->')
            #                             with a.tr():
            #                                 a.td(height='12', style='height: 12px; font-size: 0px; line-height: 0;', valign='top', **{'aria-hidden': 'true'})
            #                             a('<!-- end space -->')

def add_opportunities(a, opportunities):
    if not opportunities:
        return

    add_opportunities_section_header(a)
    for opportunity in opportunities:
        add_opportunity(a, opportunity)
