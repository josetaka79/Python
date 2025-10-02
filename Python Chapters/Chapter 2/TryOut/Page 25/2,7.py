
# Name with whitespace characters (\t for tab, \n for newline)
name="\t Josephine Anucha \n"

# Print the name as is (with whitespace)
print("Original name with whitespace:")
print(name)

# Remove whitespace from the left
print("\nUsing 1strip():")
print(name.lstrip())

# Remove whitespace from the right
print("\nUsing rstrip():")
print(name.rstrip())

# Remove whitespace from both sides
print("\nusing strip():")
print(name.strip())
