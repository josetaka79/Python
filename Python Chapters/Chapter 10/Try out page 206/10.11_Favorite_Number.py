# This program asks the user for their favorite number
# and saves it in a JSON file called favorite_number.json

import json
from pathlib import Path

# Ask the user for their favorite number
favorite_number = input("What is your favorite number? ")

# Convert the number to JSON format (so it can be stored safely as text)
content = json.dumps(favorite_number)

# Create a Path object for the file favorite_number.json
path = Path("favorite_number.json")

# Write the JSON string to the file
path.write_text(content)

print("Thanks! I've saved your favorite number.")