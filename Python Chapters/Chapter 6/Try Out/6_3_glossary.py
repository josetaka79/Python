# Create a dictionary to store programming terms and their meanings
# Keys are programming terms, values are their definitions
glossary = {
    "variable": "A container for storing data values.",          # Term: variable
    "List": "A collection of items in a particular order.",      # Term: List
    "Dictionary": "A collection of key-value pairs.",           # Term: Dictionary
    "Loop": "A structure for repeating a block of code multiple times.",  # Term: Loop
    "Function": "A block of code that performs a specific task." # Term: Function
}

# Print a header for the glossary
print("Programming Glossary:\n")

# Loop through each key-value pair in the dictionary
# items() returns each term and its meaning as a tuple
for word, meaning in glossary.items():
    # Print the term followed by its definition
    # \n adds a new line, \t adds a tab space for neat formatting
    print(f"{word}:\n\t{meaning}\n")