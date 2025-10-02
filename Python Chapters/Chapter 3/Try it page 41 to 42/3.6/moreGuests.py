# Create an initial list of guests
Guest = ["Ncha", "Khan", "Fru", "Anucha", "Desmond"]

# The following lines were commented out: printing specific guests at index 2 and 3
# print(Guest[2])
# print(Guest[3])

# Remove the guests at index 2 and 3 ("Fru" and "Anucha")
del Guest[2]  # Removes "Fru"
del Guest[3]  # Removes "Desmond" (after the previous deletion, the indexes shift)

# Insert a new guest "Edith" at index 2
Guest.insert(2, "Edith")
print(Guest)  # Print the updated list

# Insert another new guest "Nchang" at index 3
Guest.insert(3, "Nchang")
print(Guest)  # Print the updated list

# Reassign the Guest list to the final ordered list
Guest = ["Ncha", "Khan", "Edith", "Nchang", "Desmond"]
print(Guest)  # Print the final list

# Loop through each guest to create a personalized message
for guest in Guest:
    # Create a message stating that a bigger table was found
    message = f"I found a bigger table, {guest}."
    
    # Print the message for each guest
    print(message)
  