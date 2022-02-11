import re

def convert_to_id(name):
    id = name.strip()
    id = re.sub(r"[^\w\s]", '', name)
    id = re.sub(r"\s+", '-', name)
    return id
