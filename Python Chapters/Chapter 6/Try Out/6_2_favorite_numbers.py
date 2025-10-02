# Create a dictionary to store people's favorite numbers
# Keys are the names of people, and values are their favorite numbers
favorite_numbers = {
    "Irine": 5,     # Key: 'Irine', Value: 5
    "Ncha": 9,      # Key: 'Ncha', Value: 9
    "Anucha": 10,   # Key: 'Anucha', Value: 10
    "Fru": 12,      # Key: 'Fru', Value: 12
    "Khan": 14      # Key: 'Khan', Value: 14
}

# Loop through the dictionary to print each person's favorite number
# items() returns key-value pairs as tuples
for name, number in favorite_numbers.items():
    # Use an f-string to format the output nicely
    print(f"{name}'s favorite number is {number}.")