# app.py
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
        
        # Generate newsletter
        output_file = generate_newsletter(events, articles, opportunities)
        
        # Return the file path
        return jsonify({'success': True, 'file': output_file})
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/download', methods=['GET'])
def download():
    file_path = 'soc-announce.html'
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({'success': False, 'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)