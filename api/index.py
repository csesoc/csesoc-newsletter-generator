from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import sys
from scrapers.facebook import Event
from scrapers.media import Article
from scrapers.opportunities import Opportunity
from main import generate_newsletter

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

@app.route('/generate', methods=['POST'])
def generate():
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