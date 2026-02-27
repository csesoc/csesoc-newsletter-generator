from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import sys
from .scrapers.facebook import Event
from .scrapers.media import Article
from .scrapers.opportunities import Opportunity



# MAIN.PY

from airium import Airium

from .scrapers.facebook import get_upcoming_events, man_get_upcoming_events
from .scrapers.media import get_articles, man_get_articles
from .scrapers.opportunities import get_opportunities, man_get_opportunities

from .newsletter.styles import LIGHT_GREY
from .newsletter.header import add_header
from .newsletter.events import add_events
from .newsletter.articles import add_articles
from .newsletter.opportunities import add_opportunities
from .newsletter.footer import add_footer

TABLE_KWARGS = {
    "width": "100%",
    "cellpadding": "0",
    "cellspacing": "0",
}

VALID_CMD_LEN = {1, 2}

def generate_newsletter(facebook_events, media_articles, opportunities, save_file=True):
    a = Airium()
    a("<!DOCTYPE html>")
    with a.html(
        xmlns="http://www.w3.org/1999/xhtml",
        **{
            "xmlns:o": "urn:schemas-microsoft-com:office:office",
            "xmlns:v": "urn:schemas-microsoft-com:vml",
        },
    ):

        # Some email clients strip away the `<head>`, so sometimes fonts and stylesheets won't get loaded.
        # Try to use inline styling instead of relying on styling in `<head>`
        with a.head():
            a.title(_t="soc-announce")
            a.meta(content="IE=edge", **{"http-equiv": "X-UA-Compatible"})
            a.meta(content="text/html; charset=UTF-8", **{"http-equiv": "Content-Type"})
            a.meta(content="width=device-width, initial-scale=1", name="viewport")

            # Fonts
            a.link(
                href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700",
                rel="stylesheet",
                type="text/css",
            )
            a.link(
                href="https://fonts.googleapis.com/css2?family=Ubuntu+Mono&display=swap",
                rel="stylesheet",
                type="text/css",
            )

        # Nesting content in at least two tables deep is best practice
        with a.body().table(id="bodyTable", width="100%"):
            with a.tr().td(align="center").table(
                id="emailContainer",
                width="800",
                cellpadding="50",
                cellspacing="0",
                style=f"background: {LIGHT_GREY};",
            ):
                with a.tr().td().table(
                    id="emailContent",
                    width="700",
                    cellpadding="0",
                    cellspacing="0",
                    style="background: white;",
                ):
                    with a.thead():
                        with a.tr().td().table(id="emailHeader", **TABLE_KWARGS):
                            with a.tr().td():
                                add_header(a)
                    with a.tbody():
                        with a.tr().td().table(id="emailBody", **TABLE_KWARGS):
                            with a.tr().td().table(id="upcomingEvents", **TABLE_KWARGS):
                                with a.tr().td():
                                    add_events(a, facebook_events)
                            with a.tr().td().table(id="mediaArticles", **TABLE_KWARGS):
                                with a.tr().td():
                                    add_articles(a, media_articles)
                            with a.tr().td().table(id="opportunities", **TABLE_KWARGS):
                                with a.tr().td():
                                    add_opportunities(a, opportunities)
                    with a.tfoot():
                        with a.tr().td().table(id="emailFooter", **TABLE_KWARGS):
                            with a.tr().td():
                                add_footer(a)

    if save_file:
        with open("soc-announce.html", "w") as f:
            f.write(str(a))
        return "soc-announce.html"

    return str(a)




app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def index():
    """Root endpoint that returns a welcome message."""
    return jsonify({
        'message': 'Hi! Welcome to the CSESoc Newsletter Generator API',
        'endpoints': {
            'POST /generate': 'Generate a newsletter from provided events, articles, and opportunities'
        }
    })

@app.route('/generate', methods=['GET', 'POST', 'OPTIONS'])
def generate():
    # Handle preflight CORS requests
    if request.method == 'OPTIONS':
        return jsonify({'success': True}), 200
    try:
        data = request.json
        
        # Convert JSON data to Python objects
        events = [Event(
            url=event['url'],
            title=event['title'],
            description=event['description'],
            time=event['time'],
            location=event['location'],
            img=event['img']
        ) for event in data.get('events', [])]
        
        articles = [Article(
            url=article['url'],
            title=article['title'],
            description=article['description'],
            img=article['img']
        ) for article in data.get('articles', [])]
        
        opportunities = [Opportunity(
            title=opportunity['title'],
            description=opportunity['description']
        ) for opportunity in data.get('opportunities', [])]
        
        # Generate newsletter without saving to file
        output_str = generate_newsletter(events, articles, opportunities, save_file=False)
        
        # Return the HTML content directly
        return jsonify({'success': True, 'html': output_str})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)