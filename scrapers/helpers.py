def remove_attrs(soup, whitelist=["href", "target"]):
    for attr in [attr for attr in soup.attrs if attr not in whitelist]:
        del soup[attr]

    for tag in soup.findAll(True):
        for attr in [attr for attr in tag.attrs if attr not in whitelist]:
            del tag[attr]
