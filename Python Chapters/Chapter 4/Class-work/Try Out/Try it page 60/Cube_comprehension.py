# Create a list of cubes using list comprehension
# value**3 calculates the cube of each number (value raised to the power of 3)
# range(1, 10) generates numbers from 1 to 9 (10 is not included)
cubes = [value**3 for value in range(1, 10)]

# Print the list of cubes
print(cubes)