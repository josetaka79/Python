# Create a list of guests who are still invited
Guest = ["Fru", "Khan"]

# Print the current guest list to verify its contents
print(Guest)

# Loop through each guest in the list
for guest in Guest:
    # Create a message informing the guest that they are still invited
    message = f"You are still invited for dinner, {guest}"
    
    # Print the message for each guest
    print(message)