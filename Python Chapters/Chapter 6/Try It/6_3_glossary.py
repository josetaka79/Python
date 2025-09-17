# Create a dictionary with programming terms and their meanings
glossary ={
    "variable": "A container for storing data values.",
    "List": "A collection of items in a particular order.",
    "Dictionary": "A collection of key-value pairs.",
    "Loop": "A structure for repeating a block of code multiple times.",
    "Function": "A block of code that performs a specific task."
}

# print each word and its meaning with neat formating
print("Programming Glossary:\n")
for word, meaning in glossary.items():
    print(f"{word}:\n\t{meaning}\n")