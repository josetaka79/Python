# This program reads a text file and counts the approximate number of words in it.
from pathlib import Path
# Define the path to the file 'alice.txt'
path = Path('C:/Users/User/OneDrive/Desktop/Code college/Python/Python  source code/Chapters/Chapter 10/Guest.txt')

# Ask the user for their name
name = input("Please enter your name: ")

# Open (or create) the file guest.txt in write mode
#with open("guest.txt", "w") as file:
path.write_text(name+ "\n")

print(f"Thank you, {name}. Your name has been recorded in guest.txt.")