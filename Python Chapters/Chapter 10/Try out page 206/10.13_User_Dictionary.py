# This program collects multiple pieces of information about a user,
# stores it in a dictionary, saves it to a JSON file,
# then reads it back and displays a summary.

import json
from pathlib import Path

# Define the path to the JSON file
path = Path("user_info.json")

# Check if the file already exists and has data
if path.exists() and path.read_text().strip() != "":
    # Read the JSON data from the file
    content = path.read_text()
    user_info = json.loads(content)
    print("I already know the following about you:")
else:
    # File doesn't exist or is empty, so ask for user information
    username = input("Enter your username: ")
    age = input("Enter your age: ")
    favorite_color = input("Enter your favorite color: ")

    # Store all information in a dictionary
    user_info = {
        "username": username,
        "age": age,
        "favorite_color": favorite_color
    }

    # Convert the dictionary to a JSON string and save it
    content = json.dumps(user_info)
    path.write_text(content)
    print("Thanks! I've saved your information.")

# Display a summary of what the program remembers
print("\nSummary of stored information:")
for key, value in user_info.items():
    print(f"{key.capitalize()}: {value}")