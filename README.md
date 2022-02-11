# CSESoc Newsletter Generator
## Quickstart

1. Export CSESoc Opportunities Sheet as a HTML file and place `Form responses 1.html` into your root directory.
2. Run `python3 main.py` in root directory and it will generate `soc-announce.html`. This file contains scraped data, so we need to double check its in a presentable format.
3. Shorten the event descriptions to something presentable. Try not to go over double the height of the cover photo.
4. Shorten the article descriptions, usually they are already quite short though.
5. Ensure the titles for opportunities are actually the roles offered, and that the descriptions aren’t too long. If there is an apply link, add a **Call to Action link** saying “Apply now” or something similar.
6. Open HTML file in Chrome, and select all (use `CTRL` + `A`)
7. Paste into Gmail and send the email:
  - TO: `soc-announce@cse.unsw.edu.au`
  - FROM: `secretary@csesoc.org.au`
  - SUBJECT: `[CSESoc] Newsletter Term 1 Week 1`

## How it works

Upcoming events are scraped from CSESoc UNSW’s Facebook Page. We scrape from the mobile version of the page because it doesn’t rely on JavaScript to dynamically load the page, making it easier to scrape. For each upcoming event we retrieve the title, description, time, location and cover photo.

Media articles are scraped from the Media Website. All the latest articles along with their descriptions are on the home page, making it very easy.

Opportunities can’t be scraped easily, because the data exists on a Google Sheets and the effort to verify your account access is such a cbbs. Instead, we export the sheet in a HTML format and scrape the information from the local HTML file. We use HTML instead of CSV because it preserves new lines and paragraphs.

Now that we have all our data, the script writes it up nicely into a HTML file. However, the scraped descriptions are always usually too long, so that’s why we need to make some manual changes once the HTML file has been made.

## Email HTML

Due to different email client, there are over 15000 ways an email can be rendered o_O

Some email clients strip away `<head>` when rendering the content, meaning no custom fonts or specified styling. This is why you must use inline styling.

Some email client’s don’t render `<div>` properly, only tables lmao. Stick to `<table>`, `<tr>` and `<td>` if you want to edit the layout.

Images must always be hosted somewhere else, and linked using its URL. Usually right clicking the image and clicking “Open image in new tab” is enough to find the URL, but you can also store it on Imgur or similar image hosting sites.

Use [https://www.htmlemailcheck.com/check/](https://www.htmlemailcheck.com/check/) to check whether your HTML tags will be rendered correctly.

## Other newsletters to take inspiration from

- Arc Student News
- Engscope (they have cool gifs and change their headers in every edition :O)
