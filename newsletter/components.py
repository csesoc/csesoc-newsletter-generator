from newsletter.styles import BUTTON


def add_divider(a):
    a.p(style='border-top:dashed 1px lightgrey;font-size:1;margin:0px auto;width:100%;padding-bottom:15px;')

def add_section_header(a, section_name):
    with a.div(style='background:#ffffff;background-color:#ffffff;Margin:0px auto;max-width:600px;'):
        with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='background:#ffffff;background-color:#ffffff;width:100%;'):
            with a.tbody():
                with a.tr():
                    with a.td(style='direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;'):
                        with a.div(klass='mj-column-px-500 ', style='font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;'):
                            with a.table(border='0', cellpadding='0', cellspacing='0', role='presentation', style='vertical-align:top;', width='100%'):
                                with a.tr():
                                    with a.td(align='center', style='font-size:0px;padding:10px 25px;word-break:break-word;'):
                                        with a.div(style='text-transform:uppercase;font-family:Helvetica;font-size:20px;font-weight:bold;line-height:1;text-align:center;color:#000000;'):
                                            a(section_name)
                                with a.tr():
                                    with a.td(align='center', style='font-size:0px;padding:0px 0px;word-break:break-word;'):
                                        with a.div(style='font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:25px;font-weight: bold;line-height:1;text-align:center;color:#1051ea;'):
                                            a('___')

def add_button(a, url, text):
    with a.a(href=url, style='text-decoration:none;', target='_blank'):
        with a.table(style=BUTTON).tr().td():
            a(text)
        # with a.p(style='background:#1051ea;color:#ffffff;font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;font-weight:normal;line-height:200%;Margin:0;text-decoration:none;text-transform:uppercase;'):
        #     a(text)
