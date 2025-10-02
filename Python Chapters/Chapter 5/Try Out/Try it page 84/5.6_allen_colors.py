# Set the age of the person
age = 25  # The person's age

# Determine the stage of life based on the age
if age < 2:  # Check if age is less than 2
    print("The person is a baby.")  # Person is classified as a baby
elif age < 4:  # Check if age is at least 2 but less than 4
    print("The person is a toddler.")  # Person is classified as a toddler
elif age < 13:  # Check if age is at least 4 but less than 13
    print("The person is a kid.")  # Person is classified as a kid
elif age < 20:  # Check if age is at least 13 but less than 20
    print("The person is a teenager.")  # Person is classified as a teenager
elif age < 65:  # Check if age is at least 20 but less than 65
    print("The person is an adult.")  # Person is classified as an adult
else:  # If age is 65 or older
    print("The person is an elder")  # Person is classified as an elder