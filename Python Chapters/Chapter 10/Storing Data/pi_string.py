#Working with a File’s Contents
from pathlib import Path

# Define the path to the file
path = Path('C:/Users/User/OneDrive/Desktop/Code college/Python/Sedi source code/Chapters/Chapter 10/pi_digits.txt')

# Read the entire contents of the file
contents = path.read_text()

# Split the content into lines
lines = contents.splitlines()

# Initialize an empty string to hold the digits
pi_string = ''

# Loop through each line and concatenate it to pi_string
for line in lines:
    pi_string += line

# Print the concatenated string
print(pi_string)

# Print the length of the string
print(len(pi_string))