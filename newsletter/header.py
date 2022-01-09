from newsletter.styles import BLUE

BACKGROUND_IMAGE = "https://imgur.com/eQfBCYl.jpg"

def add_cover_photo(a):
    a.div(style=f'background: url({BACKGROUND_IMAGE}) top center / contain no-repeat; height: 150px;')

def add_header(a):
    add_cover_photo(a)
