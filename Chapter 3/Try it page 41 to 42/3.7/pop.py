# Create a list of guests
Guest = ["Ncha", "Khan", "Fru", "Anucha", "Desmond", "Juliet"]

# Print the initial guest list
print(Guest)

# Loop until the guest list is empty
# (Here we pop guests from the front one by one)
for guest in Guest[:]:  # Use a copy of the list to avoid modifying it while iterating
    # Originally planned invitation messages (commented out)
    # message = f"You are cordially invited for a dinner tonight, {guest}"
    # print(message)
    
    # Another planned message (commented out)
    # message = f"I can only invite 2 people for dinner {guest}"
    # print(message)
    
    # Remove the first guest from the list using pop(0)
    popped_guest = Guest.pop(0)
    
    # Optionally, print the updated guest list or the removed guest
    # print(Guest)
    # print(popped_guest)
    
    # Create a message to apologize to the removed guest
    message = f"I am sorry, I can't invite you to dinner, {popped_guest.title()}"
    
    # Print the apology message
    print(message)