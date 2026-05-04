"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Week 14 
AI Usage: ChatGPT 
"""

import requests


def fetch_user_data(url):
    """Fetch user data from API and return JSON."""
    try:
        response = requests.get(url)

        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Request failed with status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to connect to API -> {e}")
        return None


def display_user_info(data):
    """Extract and print name and email."""
    if data:
        name = data.get("name")
        email = data.get("email")

        print(f"Name: {name}")
        print(f"Email: {email}")


def main():
    url = "https://jsonplaceholder.typicode.com/users/1"

    user_data = fetch_user_data(url)
    display_user_info(user_data)


if __name__ == "__main__":
    main()