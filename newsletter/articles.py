from newsletter.components import add_button, add_divider, add_section_header

def add_article(a, article):
    with a.div():
        with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='background:#ffffff;background-color:#ffffff;width:100%;'):
            with a.tbody():
                with a.tr():
                    with a.td(style='direction:ltr;font-size:0px;padding:5px 0;text-align:center;vertical-align:top;'):
                        with a.div(klass='mj-column-per-50 ', style='font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:50%;'):
                            with a.table(border='0', cellpadding='0', cellspacing='0', role='presentation', style='vertical-align:top;', width='100%'):
                                with a.tr():
                                    with a.td(align='left', style='font-size:0px;padding:10px;word-break:break-word;'):
                                        with a.table(align='left', border='0', cellpadding='0', cellspacing='0', role='presentation', style='border-collapse:collapse;border-spacing:0px;'):
                                            with a.tbody():
                                                with a.tr():
                                                    with a.td(style='width:280px;'):
                                                        a.img(height='auto', src=article.img, style='border:0;display:inline-block;outline:none;text-decoration:none;height:auto;width:100%;', width='280')
                        with a.div(klass='mj-column-per-50 ', style='font-size:13px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:50%;'):
                            with a.table(border='0', cellpadding='0', cellspacing='0', role='presentation', style='vertical-align:top;', width='100%'):
                                with a.tr():
                                    with a.td(align='left', style='font-size:0px;padding:9px 25px;word-break:break-word;'):
                                        with a.div(style='font-family:Helvetica;font-size:17px;font-weight:bold;line-height:1;text-align:left;color:black;'):
                                            a(article.title)
                                with a.tr():
                                    with a.td(align='left', style='font-size:0px;padding:9px 25px;word-break:break-word;'):
                                        with a.div(style='font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:1;text-align:left;color:#525252;'):
                                            a(article.description)
                                with a.tr():
                                    with a.td(align='center', style='font-size:0px;padding:10px 25px;word-break:break-word;', **{'vertical-align': 'middle'}):
                                        with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='border-collapse:separate;width:100%;line-height:100%;'):
                                            with a.tr():
                                                with a.td(align='center', bgcolor='#1051ea', role='presentation', style='border:none;border-radius:3px;cursor:auto;padding:4px 25px;background:#1051ea;color:#ffffff;font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;font-weight:normal;Margin:0;text-decoration:none;text-transform:none;', valign='middle'):
                                                    add_button(a, article.url, "Read more")

def add_articles(a, articles):
    if not articles:
        return

    add_section_header(a, "Media")
    add_divider(a)
    for article in articles:
        add_article(a, article)
        add_divider(a)
