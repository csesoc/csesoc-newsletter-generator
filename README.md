# CSESoc Newsletter Generator
## Quickstart

1. Export CSESoc Opportunities Sheet as a HTML file and place `Form responses 1.html` into your root directory.
2. Open up [https://www.facebook.com/csesoc/events](https://www.facebook.com/csesoc/events) and save this page locally to `/scrapers/cached_pages/`.
3. Run `python3 main.py` in root directory and it will generate `soc-announce.html`. This file contains scraped data, so we need to double check its in a presentable format.
4. The generated cover photos will link to your local path. Go to the Facebook event page online and open up the cover photo in a new tab and directly link the `src` to this link.
5. Shorten the event descriptions to something presentable. Try not to go over double the height of the cover photo.
6. Shorten the article descriptions, usually they are already quite short though.
7. Ensure the titles for opportunities are actually the roles offered, and that the descriptions aren’t too long. If there is an apply link, add a **Call to Action link** saying “Apply now” or something similar.
8. Open HTML file in Chrome, and select all (use `CTRL` + `A`)
9. Paste into Gmail and send the email:
  - TO: `soc-announce@cse.unsw.edu.au`
  - FROM: `secretary@csesoc.org.au`
  - SUBJECT: `[CSESoc] Newsletter Term 1 Week 1`

## How it works

Upcoming events are scraped from CSESoc UNSW’s Facebook Page. We scrape from the mobile version of the page because it doesn’t rely on JavaScript to dynamically load the page, making it easier to scrape. For each upcoming event we retrieve the **title, description, time, location** and **cover photo**.

![image](https://github.com/csesoc/csesoc-newsletter-generator/assets/79000337/9db415c6-a1ff-4727-8fac-232d8e04cc61)
          
*This is what BeautifulSoup4 sees when you scrape the iPad event page*

Since around the start Term 2 2023, Facebook requires all users to be signed in to view the upcoming events for Facebook pages. A .env file containing USERNAME and PASSWORD for an active FB account is required for the scraper to be able to log in to facebook.

Media articles are scraped from the Media Website. All the latest articles along with their descriptions are on the home page, making it very easy.

Opportunities can’t be scraped easily, because the data exists on a Google Sheets and the effort to verify your account access is such a cbbs. Instead, we export the sheet in a HTML format and scrape the information from the local HTML file. We use HTML instead of CSV because it preserves new lines and paragraphs.

Now that we have all our data, the script writes it up nicely into a HTML file. However, the scraped descriptions are always usually too long, so that’s why we need to make some manual changes once the HTML file has been made.



### Breaking changes from Facebook
(Fixed as of Term 2 2023)
~~This used to be quite automated. However, since around the start of Term 3 of 2022, users that are not logged in cannot see a page's upcoming events, regardless whether the event or page is public. This is why we must now provide the script a saved local copy of [https://www.facebook.com/csesoc/events](https://www.facebook.com/csesoc/events).~~ 

~~The script can still request event details from any event page - it is only the page showing all upcoming events that is now disabled.~~

## Email HTML

Due to different email client, there are over 15000 ways an email can be rendered o_O

Some email clients strip away `<head>` when rendering the content, meaning no custom fonts or specified styling. This is why you must use inline styling.

Some email client’s don’t render `<div>` properly, only tables lmao. Stick to `<table>`, `<tr>` and `<td>` if you want to edit the layout.

Images must always be hosted somewhere else, and linked using its URL. Usually right clicking the image and clicking “Open image in new tab” is enough to find the URL, but you can also store it on Imgur or similar image hosting sites.

Use [https://www.htmlemailcheck.com/check/](https://www.htmlemailcheck.com/check/) to check whether your HTML tags will be rendered correctly.

## Other newsletters to take inspiration from

- Arc Student News
- Engscope (they have cool gifs and change their headers in every edition :O)
