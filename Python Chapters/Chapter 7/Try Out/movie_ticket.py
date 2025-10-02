# Start an infinite loop to keep asking for user input
while True:
    # Ask the user to enter their age or quit
    age_input = input("Enter your age ( or type 'quit' to stop):")
    
    # Check if the user wants to stop the program
    if age_input.lower() == 'quit':
        print("Thank you for using the ticket system. Goodbye!")
        break
        
        # validate input: make sure the user entered a number
    if age_input.isdigit():
        # print("Invalid input. Please enter a number or 'quit'. ")
        # Go back to the beginning of the loop
    
        # Convert the input to an integer (since age must be a number)
        age= int(age_input)
        
        # Determine the ticket price based on age
        if age < 3:
         print (f"Your ticket is free!\n")
        elif age <= 12: # between 3 and 12
         print("Your ticket is $10.")
        else: # over 12
         print("Your ticket is $15.")