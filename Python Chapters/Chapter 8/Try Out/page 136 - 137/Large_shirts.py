# Define the function with default size = "Large" and default message = "I love Python"
def make_shirt(size="Large", message="I love Python"):
    print(f"\nA {size}-sized shirt will be made with the message: '{message}'")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="Medium")

# Make a shirt of any size (e.g., Small) with a different message
make_shirt(size="Small", message="Keep coding and never give up!")