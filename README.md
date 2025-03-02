# CSESoc Newsletter Generator

## Browser-Use Web-UI Prompt

### Task Description

Go to https://zitianqin.com/csesoc-newsletter-generator/ to generate the CSESoc Newsletter for the week between Monday March 3 to Sunday March 9 2025.

### Additional Information

To find out information about the events, go to https://www.facebook.com/csesoc/events and visit each event page for every event within the week period from Monday to Sunday. Please put the time in the following format in the generator: e.g. 27 JAN 10-8:30PM. For the image link, please copy the facebook event banner image link and paste it into https://imgur.com/upload to upload it, and then right click on the uploaded image to copy the png or jpeg url of the image before inserting it into the newsletter generator.

To find out information about media, go to https://media.csesoc.org.au/ and check whether any of things near the top of the home page were published within the last week. If they are, go to the page, get a short description, and add it to the generator. The image can be grabbed from the page top as well. Then, go to https://www.youtube.com/c/csesocunsw/videos and check if any of the videos were uploaded in the last week. If they were, do a similar thing, and use the thumbnail of the youtube video as the image link.

To find out information about opportunities, keep in mind that if any of them are unpaid work-related jobs or internships, make the title in the generator say in capital letters that it's unpaid. Go to https://docs.google.com/spreadsheets/d/1d0IPh9fX-lV7zHxabuTf-rph_NItUqCWIW0yXz6YAdk and check if any new requests came though in the last week. Add them to the newsletter generator. (you can include the entire description). Then, go to https://mail.google.com/mail/u/1/#inbox and check if any emails offering opportunities or asking for promotions to the student society there were not in the opportunities form, and add the details from there to the newsletter generator as well.

If any of the sections do not have any events, media, or opportunities, feel free to leave them blank.

## Quickstart

1. Export CSESoc Opportunities Sheet as a HTML file and place `Form responses 1.html` into your root directory.
2. Open up [https://www.facebook.com/csesoc/events](https://www.facebook.com/csesoc/events) and save this page locally to `/scrapers/cached_pages/`.
3. Run `python3 main.py [-m | -a | -gui]` in root directory and it will generate `soc-announce.html`. If the `-a` option is ran, this file contains scraped data, so we need to double check its in a presentable format. The `-m` option is a manual command-line entry, and the `-gui` option is a manual GUI entry.
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

_This is what BeautifulSoup4 sees when you scrape the iPad event page_

Since around the start Term 2 2023, Facebook requires all users to be signed in to view the upcoming events for Facebook pages. A .env file containing USERNAME and PASSWORD for an active FB account is required for the scraper to be able to log in to facebook.

Media articles are scraped from the Media Website. All the latest articles along with their descriptions are on the home page, making it very easy.

Opportunities can’t be scraped easily, because the data exists on a Google Sheets and the effort to verify your account access is such a cbbs. Instead, we export the sheet in a HTML format and scrape the information from the local HTML file. We use HTML instead of CSV because it preserves new lines and paragraphs.

Now that we have all our data, the script writes it up nicely into a HTML file. However, the scraped descriptions are always usually too long, so that’s why we need to make some manual changes once the HTML file has been made.

### Breaking changes from Facebook

~~(Fixed as of Term 2 2023)~~
This used to be quite automated. However, since around the start of Term 3 of 2022, users that are not logged in cannot see a page's upcoming events, regardless whether the event or page is public. This is why we must now provide the script a saved local copy of [https://www.facebook.com/csesoc/events](https://www.facebook.com/csesoc/events).

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
