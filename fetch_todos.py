"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 3
AI Usage: ChatGPT 
"""
import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/todos"

def fetch_todos():
    try:
        response = requests.get(url)

        # Check request success
        if response.status_code != 200:
            print("Request failed.")
            return

        # Parse JSON
        data = response.json()

        # Extract and print first 20 titles
        count = 0

        for i, task in enumerate(data[:20], start=1):
            title = task.get("title", "No title")
            print(f"{i}. {title}")
            count += 1

        print(f"\nTotal titles printed: {count}")

    except requests.exceptions.RequestException:
        print("Request failed due to connection error.")

if __name__ == "__main__":
    fetch_todos()