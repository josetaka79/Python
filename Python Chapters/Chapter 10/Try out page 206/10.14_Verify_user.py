# This program remembers a user's username.
# If the stored username is correct, it welcomes the user back.
# If not, it asks for the correct username and updates the file.

import json
from pathlib import Path

# Define the path to the JSON file
path = Path("username.json")

def get_new_username():
    """Prompt for a new username and save it to the file."""
    username = input("Enter your username: ")
    path.write_text(json.dumps(username))
    return username

def greet_user():
    """Greet the user if the stored username is correct, otherwise get a new username."""
    if path.exists() and path.read_text().strip() != "":
        # Read the stored username
        stored_username = json.loads(path.read_text())
        print(f"Is your username '{stored_username}'? (yes/no)")
        response = input().lower()
        
        if response == "yes":
            print(f"Welcome back, {stored_username}!")
        else:
            # If not correct, get a new username
            new_username = get_new_username()
            print(f"We'll remember you, {new_username}.")
    else:
        # No username stored, so get a new one
        new_username = get_new_username()
        print(f"We'll remember you, {new_username}.")

# Run the program
greet_user()