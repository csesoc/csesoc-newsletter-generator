# Requires https://docs.google.com/spreadsheets/d/1CwL8kk3LGecT5e1x5JVYfd4f3a87hInh17wnBdBwNsY/
# to be downloaded as html file `Form responses 1.html` and saved in root directory

import os
from bs4 import BeautifulSoup

from scrapers.helpers import remove_attrs

FILE_NAME = "Form responses 1.html"

# Spreadsheet columns
TIMESTAMP = 0  # A
CONTACT_NAME = 1  # B
CONTACT_EMAIL = 2  # C
PAID_POSITION = 3  # D
OPPORTUNITY_NAME = 4  # E
DESCRIPTION = 5  # F
BENEFITS = 6  # G


class Opportunity:
    def __init__(self, title, description):
        self.title = title
        self.description = description


def get_opportunities(max=3):
    if FILE_NAME not in os.listdir("."):
        return []

    with open(FILE_NAME, "r") as file:
        soup = BeautifulSoup(file, "html.parser")
        rows = soup.find_all("tr")[-max:]
        rows.reverse()

        opportunities = []
        for row in rows:
            columns = row.find_all("td")
            title = columns[OPPORTUNITY_NAME].get_text()
            description = columns[DESCRIPTION]
            remove_attrs(description)
            description.name = "div"

            opportunities.append(Opportunity(title, description))

        return opportunities


if __name__ == "__main__":
    opportunities = get_opportunities()
    print(opportunities)
