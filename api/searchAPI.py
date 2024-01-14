from flask import Blueprint, request, jsonify
# from firebase_admin import firestore, auth
from scraperManager import G2WebScraper
search_api = Blueprint('user_api', __name__)

# db = firestore.client()
# search_ref = db.collection('past_searches')

global scraper
scraper = None

'''
POST /api/search

Description: 

JSON request body:
{
    "query": search query (string),
    "limit": max number of results to return (int),
}

JSON response body:
{
    "results": [
        {
            "name": name of company (string),
            "url": url to company page (string),
            "description": description of company (string),
            "rating": rating of company (float),
            "reviews": number of reviews of company (int),
            "categories": [
                {
                    "name": name of category (string),
                    "url": url to category page (string),
                },
                ...
            ],
            "alternatives": [
                {
                    "name": name of alternative (string),
                    "url": url to alternative page (string),
                },
                ...
            ],
        },
        ...
    ]
}
'''

@search_api.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    query = data['query']
    limit = data['limit']

    global scraper

    if scraper == None:
        scraper = G2WebScraper()
    results = scraper.getSearchResults(query, limit)

    return jsonify(results=results)
