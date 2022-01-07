BACKGROUND_IMAGE = "https://imgur.com/eQfBCYl.jpg"

def add_cover_photo(a):
    with a.div(klass='height-fix', style=f'background:url({BACKGROUND_IMAGE}) bottom center / contain no-repeat;Margin:0px auto;height:130px;'):
        with a.div(style='line-height:0;font-size:0;'):
            with a.table(align='center', border='0', cellpadding='0', cellspacing='0', role='presentation', **{'width:"100%"': ''}):
                with a.tbody():
                    with a.tr():
                        a.td(style='direction:ltr;font-size:0px;padding:20px 0;text-align:center;vertical-align:top;')

def add_header(a):
    add_cover_photo(a)
