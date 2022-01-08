# soc-announcer

1. Go to the [Opportunities Form Spreadsheet](https://docs.google.com/spreadsheets/d/1CwL8kk3LGecT5e1x5JVYfd4f3a87hInh17wnBdBwNsY/) and download as a `html` file
2. Upload this html file to the root directory (this is where it gets read)
3. From root directory run `python3 main.py` and it should write `soc-announce.html` into the root directory

## Learnings
- Due to different email client, there are over 15000 ways an email can be rendered O.O
- Always use inline CSS because sometimes the `<head>` (which includes the CSS stylesheet) is removed, leaving only the `<body>`
  - [https://customer.io/blog/how-to-make-css-play-nice-in-html-emails-without-breaking-everything/](https://customer.io/blog/how-to-make-css-play-nice-in-html-emails-without-breaking-everything/)
- Always use `<table>` because it ensures tehy will look good across all devices
- `<hr>` don't render well in email HTML
- Every `<tr>` needs a `<td>` inside

## Examples
- Arc Student Life newsletters
- Engscope

## Useful Links
- [https://www.htmlemailcheck.com/check/](https://www.htmlemailcheck.com/check/)

## Things to do
- gif soc-announce cover photo, gotta look cool!
- check dark mode outlook doesn't fuck it up
- scrape opportunities form
