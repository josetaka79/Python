# Create a list of guests
Guest = ["Ncha", "Khan", "Fru", "Anucha", "Desmond", "Juliet"]

# Print the entire guest list to check its contents
print(Guest)

# Loop through each guest in the list
for guest in Guest:
    # Create a personalized invitation message for each guest using an f-string
    message = f"You are cordially invited for a dinner tonight, {guest}"
    
    # Print the invitation message
    print(message)