import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
print(f"Loaded API Key: {NEWS_API_KEY}")
BASE_URL = "https://newsapi.org/v2"

def fetch_top_headlines(country="us", category=None):
    """Fetch top headlines from News API"""
    url = f"{BASE_URL}/top-headlines"
    
    params = {
        "apiKey": NEWS_API_KEY,
        "country": country,
        "pageSize": 10
    }
    if category:
        params["category"] = category

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        return None