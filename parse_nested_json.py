"""
Mikayla Settles-Chambers
CMSC 111
Spring 2026
Assignment 4
AI Usage: ChatGPT 
"""
import json

def parse_data():
    try:
        with open("nested_data.json", "r") as file:
            data = json.load(file)

        # Extract values
        name = data["student"]["name"]
        email = data["student"]["contact"]["email"]
        city = data["student"]["address"]["city"]
        first_course = data["student"]["courses"][0]["course_name"]
        second_course_grade = data["student"]["courses"][1]["grade"]

        # Print results
        print(f"Student Name: {name}")
        print(f"Email: {email}")
        print(f"City: {city}")
        print(f"First Course: {first_course}")
        print(f"Second Course Grade: {second_course_grade}")

    except (KeyError, IndexError, FileNotFoundError, json.JSONDecodeError):
        print("Missing data in JSON file.")

if __name__ == "__main__":
    parse_data()