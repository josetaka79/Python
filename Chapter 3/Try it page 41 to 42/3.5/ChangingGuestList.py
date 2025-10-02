# Create a list of guests
Guest = ["Ncha", "Khan", "Fru", "Anucha", "Desmond"]

# The following lines were commented out: printing specific guests
# print(Guest[2])
# print(Guest[3])

# Remove the guests at index 2 and 3 ("Fru" and "Anucha")
del Guest[2]
del Guest[3]

# Insert new guests at specific positions
Guest.insert(2, "Edith")   # Add "Edith" at index 2
print(Guest)               # Print the updated list

Guest.insert(3, "Nchang")  # Add "Nchang" at index 3
print(Guest)               # Print the updated list

# Reassign the Guest list to a new ordered list
Guest = ["Ncha", "Khan", "Edith", "Nchang", "Desmond"]
print(Guest)               # Print the final list

# Loop through each guest and create a personalized dinner invitation
for guest in Guest:
    message = f"You are invited for a dinner tonight, {guest}."  # Create the invitation message
    print(message)  # Print the invitation
