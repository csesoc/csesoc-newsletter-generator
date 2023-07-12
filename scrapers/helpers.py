def remove_attrs(soup, whitelist=["href", "target"]):
    for attr in [attr for attr in soup.attrs if attr not in whitelist]:
        del soup[attr]

    for tag in soup.findAll(True):
        for attr in [attr for attr in tag.attrs if attr not in whitelist]:
            del tag[attr]


HEADERS = {'fireFox': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0',
           'iPad': 'Mozilla/5.0 (iPad; CPU OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPad7,5;FBMD/iPad;FBSN/iOS;FBSV/14.4.2;FBSS/2;FBID/tablet;FBLC/;FBOP/5]'}
