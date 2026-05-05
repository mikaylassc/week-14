"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 14 
AI Usage: ChatGPT 
"""

import os
import requests

# API used: NewsAPI.org

def fetch_latest_news():
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("API key not found. Please set your API key.")
        return

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "pageSize": 10,
        "apiKey": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print(f"Error: request failed. Status code: {response.status_code}")
        return

    data = response.json()
    articles = data.get("articles", [])

    if not articles:
        print("No articles returned.")
        return

    for i, article in enumerate(articles, start=1):
        title = article.get("title", "No title")
        published = article.get("publishedAt", "No date")

        print(f"{i}. Headline: {title} Published: {published}")


if __name__ == "__main__":
    fetch_latest_news()
    