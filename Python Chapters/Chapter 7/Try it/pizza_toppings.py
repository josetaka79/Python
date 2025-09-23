# Keep asking the user to enter pizza toppings until they type 'quit'
while True:
    # Prompt the user to input a topping
    topping = input("Enter a pizza topping (or type 'quit' to stop): ")

    # Check if the user entered 'quit' (case-insensitive with .lower())
    if topping.lower() == 'quit':
        # Inform the user that no more toppings will be added
        print("Finished adding toppings to your pizza!")
        # Break out of the loop to stop asking for more input
        break
    else:
        # If the user entered something other than 'quit',
        # print a confirmation message
        print(f"I'll add {topping} to your pizza.")