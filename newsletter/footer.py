
def add_sponsors(a):
    with a.div(klass='height-fix-sponsor', style='background:url(https://i.imgur.com/XvCLqIg.png) bottom center / contain no-repeat;Margin:0px auto;max-width:600px;height:315px;'):
        with a.div(style='line-height:0;font-size:0;'):
            with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='background:top center / contain no-repeat;width:100%;'):
                with a.tbody():
                    with a.tr():
                        a.td(style='direction:ltr;font-size:0px;padding: 0px 0;text-align:center;vertical-align:top;')
    with a.div(style='background:#3c54ec;background-color:#3c54ec;Margin:0px auto;max-width:600px;'):
        with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='background:#3c54ec;background-color:#3c54ec;width:100%;'):
            with a.tbody():
                with a.tr():
                    with a.td(style='direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;'):
                        with a.div(style='font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:1;text-align:center;color:white;text-decoration:none!important;'):
                            a('2021 Sponsors')

def add_socials(a):
    with a.div(style='background:#f0f0f0;background-color:#f0f0f0;Margin:0px auto;max-width:600px;'):
        with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', style='background:#f0f0f0;background-color:#f0f0f0;width:100%;'):
            with a.tbody():
                with a.tr():
                    with a.td(style='direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;'):
                        with a.div(style='font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:3;text-align:center;color:#888888;'):
                            a.a(href='https://www.facebook.com/csesoc', style='color:#888888;', _t='Facebook Page')
                            a('|')
                            a.a(href='https://www.facebook.com/groups/csesoc/', style='color:#888888;', _t='Facebook Group')
                            a('|')
                            a.a(href='https://www.linkedin.com/company/csesoc/about/', style='color:#888888;', _t='LinkedIn')
                        with a.div(style='font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:3;text-align:center;color:#888888;'):
                            a('Contact:')
                            a.b(_t='csesoc@csesoc.org.au')
                        with a.div(style='font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:3;text-align:center;color:#888888;'):
                            a('If you do not wish to receive our newsletters,')
                            with a.a(href='https://status.cse.unsw.edu.au/Control_Panel/Mail/Mailing_List_Subscriptions/', style='color:#888888;', target='_blank'):
                                a.b(_t='unsubscribe here')
                            a('.')

def add_footer(a):
    add_sponsors(a)
    add_socials(a)
