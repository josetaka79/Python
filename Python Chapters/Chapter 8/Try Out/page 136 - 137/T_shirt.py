def make_shirt(size="Large", message="I love Python"):
    print(f"\nA {size}-sized shirt will be made with the message: '{message}'")

# Call the function using positional arguments
make_shirt("Medium", "Code is life!")

# Call the function using keyword arguments
make_shirt(size="Small", message="Keep coding!")

# Call the function without providing arguments (defaults will be used)
make_shirt()
    
    
    