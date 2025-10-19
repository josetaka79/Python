# This program remembers the user's favorite number using a JSON file.
# If the number is already stored, it displays it.
# If not, it asks for the number and stores it for next time.

import json
from pathlib import Path

# Define the path to the JSON file
path = Path("favorite_number.json")

# Check if the file already exists and has content
if path.exists() and path.read_text().strip() != "":
    # Read the number from the file
    content = path.read_text()
    favorite_number = json.loads(content)
    print(f"I know your favorite number! It's {favorite_number}.")
else:
    # Ask for the user's favorite number
    favorite_number = input("What is your favorite number? ")

    # Convert the number to JSON and save it to the file
    content = json.dumps(favorite_number)
    path.write_text(content)

    print("Thanks! I'll remember your favorite number next time.")