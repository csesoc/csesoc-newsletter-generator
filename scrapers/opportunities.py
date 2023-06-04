# Requires https://docs.google.com/spreadsheets/d/1CwL8kk3LGecT5e1x5JVYfd4f3a87hInh17wnBdBwNsY/
# to be downloaded as html file `Form responses 1.html` and saved in root directory

import os
from bs4 import BeautifulSoup

from scrapers.helpers import remove_attrs

FILE_NAME = "Form responses 1.html"

# Spreadsheet columns
POSTED = 0 # A
TIMESTAMP = 1  # B
CONTACT_NAME = 2  # C
CONTACT_EMAIL = 3  # D
PAID_POSITION = 4  # E
OPPORTUNITY_NAME = 5  # F
DESCRIPTION = 6  # G
BENEFITS = 7  # H


class Opportunity:
    def __init__(self, title, description):
        self.title = title
        self.description = description


def get_opportunities(max=6):
    if FILE_NAME not in os.listdir("."):
        return []

    with open(FILE_NAME, "r") as file:
        soup = BeautifulSoup(file, "html.parser")
        rows = soup.find_all("tr")[-max:]
        rows.reverse()

        opportunities = []
        for row in rows:
            columns = row.find_all("td")
            if len(columns) < 8:
                continue
            title = columns[OPPORTUNITY_NAME].get_text()
            description = columns[DESCRIPTION]
            remove_attrs(description)
            description.name = "div"

            if title != "Opportunity Name " and title != "":
                opportunities.append(Opportunity(title, description))

        return opportunities


if __name__ == "__main__":
    opportunities = get_opportunities()
    print(opportunities)
