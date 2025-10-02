# Define the function that accepts any number of sandwich items
def make_sandwich(*items):
    print("\nYou ordered a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function three times with different numbers of arguments

# First sandwich
make_sandwich("ham", "cheese", "lettuce")

# Second sandwich
make_sandwich("turkey", "tomato")

# Third sandwich
make_sandwich("peanut butter", "jelly", "banana", "honey")