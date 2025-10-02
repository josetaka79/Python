# Create a list of guests
Guest = ["Ncha", "Khan", "Fru", "Anucha", "Desmond", "Juliet"]

# Print the entire guest list to verify its contents
print(Guest)

# Loop through each guest in the list
for guest in Guest:
    # Originally planned invitation message (commented out)
    # message = f"You are cordially invited for a dinner tonight, {guest}"
    # print(message)
    
    # New message stating that only 2 guests can be invited
    message = f"I can only invite 2 people for dinner, {guest}"
    
    # Print the message for each guest
    print(message)